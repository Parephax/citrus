from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.
def stub(request):
    return HttpResponse('This should probably go somewhere, but it doesn\'t.')
