
from django.urls import path
from pages.views import (
    HomeView,
    CreateIncidenciasView
)


urlpatterns = [
    path("", HomeView.as_view()),
    path('create-incidencias/', CreateIncidenciasView.as_view()),
]
