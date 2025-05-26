from django.shortcuts import render, HttpResponse

def pizza_food(request):
    return HttpResponse('I like pizza')

def ghormesabzi(request):
    return HttpResponse('This is Iranian food')

