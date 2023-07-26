from django.urls import path
from receitas.views import home, contato, sobre


urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # sobre
    path('contato/', contato),
]
