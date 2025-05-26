from django.shortcuts import render, HttpResponse

def tea_drink(request):
    return HttpResponse('I love it')

def coffee_drink(request):
    return HttpResponse('I do not like it')    