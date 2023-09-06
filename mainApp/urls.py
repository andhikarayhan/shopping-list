from django.urls import path

from mainApp.views import show_main

app_name = 'mainApp'

urlpatterns = [
    path('', show_main, name='show_main'),
]