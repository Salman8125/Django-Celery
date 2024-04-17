from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import test_func , send_reminder_mail

# Create your views here.

def test_route(request):
    test_func.delay()
    return HttpResponse("Test Route Hit !!")

def send_mail_to_all(request):
    send_reminder_mail.delay()
    return HttpResponse("Send Mail Route Hit !!")
