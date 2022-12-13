from django.urls import path
from  . import views # Importa todas as urls imports views

urlpatterns = [
    path('', views.index, name='index'),
]