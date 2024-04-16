from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import test_func

# Create your views here.

def test_route(request):
    test_func.delay()
    return HttpResponse("Test Route Hit !!")
