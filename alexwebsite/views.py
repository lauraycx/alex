from django.shortcuts import render, redirect
from django.urls import reverse

def homepage(request):
    if request.method == 'GET':
        return render(request, 'alexwebsite/homepage.html', {})

