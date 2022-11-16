from django.shortcuts import render

# Create your views here.

def home(response):
    return render(response, "staticpages/home.html", {})

def about(response):
    return render(response, "staticpages/about.html", {})

def calendar(response):
    return render(response, "staticpages/calendar.html", {})

def testtournament(response):
    return render(response, "staticpages/testtournament.html", {})