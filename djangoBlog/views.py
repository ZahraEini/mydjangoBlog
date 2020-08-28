from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse("Hi there! I'm hello world!")
    return render(request , 'about.html')
def home(request):
    #return HttpResponse('home')
    return render(request , 'Home.html')
