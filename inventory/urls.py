from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inventory, name='home_page')
]

