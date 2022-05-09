from django.urls import path
from .views import Chatbot

urlpatterns = [
    path('chatbot/', Chatbot.as_view(), name = 'chatbot_test'),
]