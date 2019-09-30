from django.shortcuts import render
from django.http import HttpResponse #header files

# Create your views here.
def indexpage(request):             #function
    return HttpResponse("Welcome")
def contact(request):
    return HttpResponse("Contact page")
def home(request):
    return HttpResponse("Welcome to my home page")