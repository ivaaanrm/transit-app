# views.py

from django.forms import ValidationError
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Incidencia



class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visible_incidencias = Incidencia.objects.filter(visible=True)
        context["incidencias"] = visible_incidencias
        return context


class CreateIncidenciasView(APIView):
    """
    API endpoint to create multiple Incidencia instances.
    """

    def post(self, request):
        """
        Takes a POST request with JSON data and saves each entry as an Incidencia instance.
        """

        parser = JSONParser()
        data = parser.parse(request)
        
        if not isinstance(data, list):
            return Response({'error': 'Invalid data format. Expecting a list of incident objects.'}, status=status.HTTP_400_BAD_REQUEST)

        Incidencia.objects.all().update(visible=False)
        for item in data:
            # if not all(key in item for key in ['causa', 'zonq', 'via', 'longitud']):
            #     return Response({'error': 'Missing required fields for some incidents.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate individual fields if needed (e.g., length restrictions)
            # ...
            try:
                incidencia = Incidencia.objects.create(**item)
            except Exception as e:
                return Response({'error': f'Validation error: {e}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Incidencias created successfully.'}, status=status.HTTP_201_CREATED)

