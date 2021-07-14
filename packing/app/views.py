from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('app success')


def check_service(request):
    
    return None