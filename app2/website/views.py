from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def home(req):
    return render(req,"web/index.html")
def contact(req):
    return render(req,"web/contact.html")
def gallery(req):
    return render(req,"web/gallery.html")
def menu(req):
    return render(req,"web/menu.html")
def research(req):
    return render(req,"web/research.html")
def services(req):
    return render(req,"web/services.html")
def about(req):
    return render(req,"web/about.html")