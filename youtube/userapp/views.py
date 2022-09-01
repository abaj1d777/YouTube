from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from asosiy.serializers import KanalSerializers,UserSerializers
from rest_framework.views import APIView
from .models import *

class KanalApi(APIView):
    def get(self, request, pk):
        k = Kanal.objects.get(id=pk)
        ser = KanalSerializers(k)
        return Response(ser.data)
    def put(self, request, pk):
        u = User.objects.get(username=request.user.name)
        kanal = Kanal.objects.get(id=pk)
        if kanal.user == u:
            malumot = request.data
            ser = KanalSerializers(kanal,data=malumot)
            if ser.is_valid():
                ser.save(user=u)
            return Response(ser.data)
        return Response()

class Users(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


