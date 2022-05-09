from django.shortcuts import render
import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class Chatbot(APIView):
    def post(self, request):
        data = request.data
        question = data['Question']

        simpleT5 = ApiConfig.model

        answer = simpleT5.predict(question)[0]

        response_dict = {"Bot: ": answer}
        return Response(response_dict, status=200)