from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status


class SignUpView(generics.GenericAPIView,):
    serializer_class = SignUpSerializer

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"message": "User created successfully",
                    "data": serializer.data}
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
