from django.shortcuts import HttpResponse, redirect, render

def home(request) :
    return render(request,"home.html")

def download(request,slug) :
    return render(request,"download.html",{"slug":slug.upper()})