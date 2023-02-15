from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

def index(request: HttpRequest) -> HttpResponse:
    random_number = random.randint(1, 100)
    context = {'random_number': random_number}
    return render(request, 'index.html', context)

def leaderboards(request: HttpRequest) -> HttpResponse:
    return render(request, 'leaderboards.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
