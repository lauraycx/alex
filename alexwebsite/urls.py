from django.urls import path
from alexwebsite import views

urlpatterns = [
    path('', views.homepage, name='home')
]