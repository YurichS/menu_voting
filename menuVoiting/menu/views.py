from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import MenuListSerializer, MenuUploadSerializer
from .models import Menu
import json


# Create your views here.

class MenuListView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Menu.objects.order_by("id").all()
    serializer_class = MenuListSerializer


class MenuUploadView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = MenuUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Menu uploaded"})

        return Response({"msg": serializer.errors})


class VoteView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        menu.votes += 1
        menu.save()
        return Response({"msg": "You voted successfully"})


class ResultView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Menu.objects.order_by('-votes').all()[:1]
    serializer_class = MenuListSerializer
