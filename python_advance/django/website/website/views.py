
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("<h1>My first website</h1>")
    return render(request, "website/homepage.html")

def aboutpage(request):
    # return HttpResponse("<h1>My about page</h1>")
    return render(request, "website/aboutpage.html")

def contactpage(request):
    # return HttpResponse("<h1>My contact page</h1>")
    return render(request, "website/contactpage.html")


