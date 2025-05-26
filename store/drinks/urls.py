from django.urls import path
from . import views

urlpatterns = [
    path('tea/', views.tea_drink),
    path('coffee/', views.coffee_drink),
]