from django.urls import path
from app.views import test_route

urlpatterns = [
    path('',test_route,name="test")
]