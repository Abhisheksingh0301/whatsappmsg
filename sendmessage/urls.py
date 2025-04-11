from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_whatsapp_message, name='send_message'),
]
