from django.urls import path
from . import views

urlpatterns = [
    path('add_film/', views.add_film, name='add_film'),
    path('', views.film_list, name='film_list'),
]