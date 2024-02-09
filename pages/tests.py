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
        'causa': 'Accident',
        'nivel': 'Calçada restringida',
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
    'causa': 'circulació',
    'nivel': 'Calçada restringida',
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
    'causa': 'obras',
    'nivel': 'Calçada restringida',
    'via': 'AP-7',
    'km_inicio_fin': '146,00 - 149,00',
    'longitud': '3,00',
    'demarcacion': 'Barcelona',
    'tramo': 'BARBERÀ DEL VALLÈS',
    'direccion': '',
    'inicio': '22:00',
    'observaciones': ''
},

      
    ]

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Incidencias creadas exitosamente!")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    test_create_incidencias()
