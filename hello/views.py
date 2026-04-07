from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django! My name is Anthony Yagoda, it is April 6, 2026, "
    "and I am learning Django in IS 218-004 - Web Application Development at NJIT.")
