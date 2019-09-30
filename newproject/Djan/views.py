from django.shortcuts import render
from django.http import HttpResponse #header files

# Create your views here.
def indexpage(request):             #function
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def home(request):
    return render(request,'home.html')