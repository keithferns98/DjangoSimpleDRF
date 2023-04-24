from django.shortcuts import render
from .serializers import SignUpSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from rest_framework.views import APIView


class SignUpView(generics.GenericAPIView,):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"message": "User created successfully",
                    "data": serializer.data}
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request,):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            response = {
                "message": "Login Successfull",
                "token": user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid Email or Password"})

    def get(sefl, request: Request):
        content = {
            "user": str(request.user),
            "token": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)
