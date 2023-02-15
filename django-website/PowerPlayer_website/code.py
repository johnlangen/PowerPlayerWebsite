from .random_number_generator import get_random_number

from django.shortcuts import render

def home(request):
    context = {'random_number': get_random_number()}
    return render(request, 'home.html', context)

