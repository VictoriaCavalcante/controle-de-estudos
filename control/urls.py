from django.urls import path

from control.views import home

urlpatterns = [
    path('', home),
]
