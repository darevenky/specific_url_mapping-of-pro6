from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def warner(request):
    return HttpResponse('SRH best cap')
