from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def leaderboards(request: HttpRequest) -> HttpResponse:
    return render(request, 'leaderboards.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')