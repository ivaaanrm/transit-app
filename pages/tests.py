from django.test import TestCase

# Create your tests here.
import requests
import json

def test_create_incidencias():
    url = "http://localhost:8001/create-incidencias/"  # Replace with your actual URL
    headers = {"Content-Type": "application/json"}

    # Example data (modify as needed)
    data = [
      {
        'causa': 'Senyalització vertical',
        'zona': 'Calçada restringida',
        'via': 'AP-7',
        'km_inicio_fin': '146,00 - 149,00',
        'longitud': '3,00',
        'demarcacion': 'Barcelona',
        'tramo': 'BARBERÀ DEL VALLÈS',
        'direccion': '',
        'inicio': '22:00',
        'observaciones': ''
    },
    {
        'causa': "Treballs d'enllumenat",
        'zona': 'Calçada tallada',
        'via': 'B-20',
        'km_inicio_fin': '6,50 - 8,00',
        'longitud': '1,50',
        'demarcacion': 'Barcelona',
        'tramo': 'BARCELONA',
        'direccion': 'DESVIAMENTS PER SORTIDA 9',
        'inicio': '01:24',
        'observaciones': 'NOCTURN 23H A 5H'
    }
    ]

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Incidencias creadas exitosamente!")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    test_create_incidencias()
