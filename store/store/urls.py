from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_to_store),
    path('hello/', views.hello),
    path('good_bay/<name>/', views.good_bay),
    path('number/', views.number_123),
    path('something/<int:num>/', views.something),
]