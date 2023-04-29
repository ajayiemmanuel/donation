from django.shortcuts import render

# Create your views here.
from .models import *




# Create your views here.

def index(request):
    context = {}
    return render (request, "charity/index.html", context)

def about(request):
    context = {}
    return render (request, "charity/about.html", context)


def appreciation(request):
    context = {}
    return render (request, "charity/appreciation.html", context)


def blog(request):
    context = {}
    return render (request, "charity/blog.html", context)

def contact(request):
    context = {}
    return render (request, "charity/contact.html", context)

def donate(request):
    context = {}
    return render (request, "charity/donate.html", context)

def support(request):
    context = {}
    return render (request, "charity/support.html", context)

def gallery(request):
    context = {}
    return render (request, "charity/gallery.html", context)

def fundraiser(request):
    context = {}
    return render (request, "charity/fundraiser.html", context)

def terms(request):
    context = {}
    return render (request, "charity/terms.html", context)

def faq(request):
    context = {}
    return render (request, "charity/faq.html", context)