from rest_framework import permissions, status
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AccountSerializer, AccountTokenObtainPairSerializer


class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccountTokenObtainPairSerializer


class Account(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Example
# @api_view(['GET'])
# @permission_classes((AllowAny,))
# @authentication_classes([])
# def hello_world(request, format=None):
    # return Response(data={'hello': 'world', 'secured': True}, status=status.HTTP_200_OK)
