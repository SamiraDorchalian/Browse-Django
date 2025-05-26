from django.shortcuts import render, HttpResponse

def welcome_to_store(request):
    return HttpResponse('Welcome to store')

def hello(request):
    full_name = 'SamiraDorchalian'
    name = 'Samira'
    family = 'Dorchalian'
    age = 26
    phone_number = age * 2
    return render(request, 'hello.html', {
        'full_name': full_name,
        'name': name,
        'family': family,
        'age': age,
        'phone_number': phone_number,
    })

def good_bay(request, name):
    return render(request, 'good_bay.html', {'name': name})

def number_123(request):
    return HttpResponse('This is the number of 123') 

def something(request, num):
    print(num)
    print(type(num))
    return HttpResponse('something')