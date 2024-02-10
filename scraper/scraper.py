from dataclasses import field
import json
import os
import asyncio
import logging
import time
from rich import print
import schedule
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict, List, Optional
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

os.chdir(os.path.dirname(__file__))

from config.config import get_params
from incidencia import Incidencia
import os
import sys
import requests


load_dotenv()
params = get_params(os.getenv("CONFIG_PATH"))
previous_results = []

def setup_logging():
    log_file_path = Path(os.getenv('PATH_LOGS'))

    # Ensure the directory exists
    log_file_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file_path,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    logging.getLogger().addHandler(console_handler)


def post_incidencias(data: List[Dict[str, str]]) ->  requests.Response:
    headers = {"Content-Type": "application/json"}    
    response = requests.post(params.API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Incidencias creadas exitosamente!")
    else:
        print("Error:", response.text)
    
    return response
    

class TransitCrawler:
    def __init__(self, url: str):
        self.url = url
        self.options = Options()
        self.setup_options()
        self.driver = self.initialize_driver()
        
        self.last_results = []

    def setup_options(self):
        if params.HEADLESS:
            self.options.add_argument("--headless")
        if params.NO_SANDBOX:
            self.options.add_argument("--no-sandbox")

    def initialize_driver(self):
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=self.options
        )

    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def fetch_html(self) -> None:
        try:
            self.driver.get(self.url)
            time.sleep(1)
            self.set_up_web_page(params.DEMARCACIONES, params.VIAS, params.OBRAS)
            time.sleep(1)
            return self.driver.page_source
        except WebDriverException as e:
            print(f"Error fetching HTML: {e}")
            return None
        
        finally:
            self.close_driver()

    def extract_data(self, html_content) -> List[Incidencia]:
        if html_content is not None:
            soup = BeautifulSoup(html_content, "html.parser")
                        
            table_id = 'taulaResultats'
            table = soup.find('table', {'id': table_id})

            traffic_results = []
            
            if table:
                # Extract information from the table
                for row in table.find('tbody').find_all('tr'):
                    columns = row.find_all('td')
                    
                    resultado = Incidencia(
                        causa = columns[0].text.strip(),
                        nivel = columns[1].text.strip(),
                        via = columns[2].find('div').text.strip(),
                        km_inicio_fin = columns[2].find_all('div')[1].text.strip(),
                        longitud = columns[3].find('div').text.strip(),
                        demarcacion = columns[4].text.strip(),
                        tramo = columns[5].text.strip(),
                        direccion = columns[6].text.strip(),
                        inicio = columns[7].find_all('div')[1].text.strip(),
                        observaciones = columns[8].text.strip(),
                    )
                    traffic_results.append(resultado)

            else:
                logging.error(f"Table with ID '{table_id}' not found.")
                print()

            return traffic_results
        else:
            logging.error(f"No se ha devuelto html")
            return []
    
    
    def set_up_web_page(self, demaraciones: List[str] = [], vias: List[str] = [], obras: bool = False) -> None:
        
        input_demarcacion = WebDriverWait(self.driver, params.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="llistaResultatsForm"]/div[1]/div/div[2]/div[2]/span/span[1]/span/ul/li/input')))
        input_vias = WebDriverWait(self.driver, params.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="llistaResultatsForm"]/div[1]/div/div[3]/div[2]/span/span[1]/span/ul/li/input')))
        
        for dema in demaraciones:
            input_demarcacion.send_keys(dema)
            input_demarcacion.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
        for via in vias:
            input_vias.send_keys(via)
            input_vias.send_keys(Keys.ENTER)
            time.sleep(1)
        
        if obras:
            checkbox = WebDriverWait(self.driver, params.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//*[@id="llistaResultatsForm:checkObres"]')))
            checkbox.click()
            
        
        button = WebDriverWait(self.driver, params.TIMEOUT).until(EC.element_to_be_clickable((By.ID, 'btnCerca')))
        button.click()




    

async def main():
    global previous_results 

    transit_crawler = TransitCrawler(params.URL)

    html = transit_crawler.fetch_html()
    resultados = transit_crawler.extract_data(html)
    logging.info(f"{len(resultados)} resultados encontrados.")
    
    if set(previous_results) == set(resultados):
        logging.info("No hay cambios")
        return
    
    previous_results = resultados    
    response = post_incidencias([incidencia.to_dict() for incidencia in resultados])    

    
    
def job():
    logging.info("Starting...")
    asyncio.run(main())

if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())

    schedule.every(params.INTERVALO).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)



    
    
