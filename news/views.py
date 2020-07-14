import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class News(APIView):
    def get(self, request):
        with open('..sample_data/news_api.json') as f:
            response = json.load(f)

        return Response(data=response, status=status.HTTP_200_OK)
