from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {"boldmessage": "This tutuorial has been put together by Sophie"}
    return render(request, 'rango/about.html', context=context_dict)

#Rango says here is the about page. Link back to home: <a href='/rango/'>Index</a>"