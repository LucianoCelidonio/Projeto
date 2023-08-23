from django.urls import path

from . import views

# urlpatterns = [
#    path('', views.home),
#    path('receitas/<int:id>/', views.receita1),
# ]


urlpatterns = [
    path('', views.home),
    path('receita/<int:id>/', views.receita1),
]
