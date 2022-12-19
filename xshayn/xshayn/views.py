from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")


