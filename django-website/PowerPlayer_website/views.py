from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
import requests

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def leaderboards(request: HttpRequest) -> HttpResponse:
    return render(request, 'leaderboards.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


def api(request):
    url = "https://api.the-odds-api.com/v4/sports/basketball_ncaab/odds/?apiKey=720de21f5e87e50813a7474461b03f06&regions=us&markets=h2h,spreads&oddsFormat=american"
    response = requests.get(url)

    if response.status_code == 200:
        data2 = response.json()

