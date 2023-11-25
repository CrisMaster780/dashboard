from django.contrib import admin
from django.urls import path, include
from .views import pedidoventa

urlpatterns = [
    path("", pedidoventa , name='pedidoventa' ),
    

]