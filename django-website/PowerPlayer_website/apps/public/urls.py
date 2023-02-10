from django.urls import path
from . import views



app_name="public"

urlpatterns = [
    path('', views.index , name="index"),
    path('leaderboards', views.leaderboards , name="leaderboards"),
    path('contact', views.contact , name="contact"),
]