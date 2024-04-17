from django.urls import path
from app.views import test_route , send_mail_to_all

urlpatterns = [
    path('',test_route,name="test"),
    path('send-mail/',send_mail_to_all,name="send_mail")
    
]