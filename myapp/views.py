from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
	return render(request, 'about.html')

def home(request):
	return render(request, 'home.html')

def gallery(request):
	return render(request, 'gallery.html')

def womens(request):
	return render(request, 'womens.html')

def kids(request):
	return render(request, 'kids.html')

def mens(request):
	return render(request, 'mens.html')