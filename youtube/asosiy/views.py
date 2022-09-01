
from rest_framework.views import APIView
from userapp.models import Kanal
from rest_framework import  generics
from .serializers import *
from rest_framework.response import Response


class VideoApiView(APIView):
    def get(self,request):
        v = Video.objects.all()
        ser = VideoSerializers(v,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = VideoSerializers(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)



class VideoApi(APIView):
    def get(self, request, pk):
        v = Video.objects.get(id=pk)
        ser = VideoSerializers(v)
        return Response(ser.data)
    def delete(self, request,pk):
        k = Kanal.objects.get(user=self.request.user)
        v = Video.objects.get(id=pk)
        if v.kanal == k:
            v.delete()
        return Response()

class ReccomendApiView(generics.ListAPIView):
    queryset =Reccomend.objects.all()
    serializer_class = ReccommendSerializers

class PrimoyApiVIew(APIView):
    def get(self,request):
        p =  Primoy.objects.all()
        ser = PrimoySerializers(p,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = PrimoySerializers(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)

class PrimoyApi(APIView):
    def get(self, request, pk):
        p = Primoy.objects.get(id=pk)
        ser = PrimoySerializers(p)
        return Response(ser.data)
    def delete(self, request,pk):
        k = Kanal.objects.get(user=self.request.user)
        p = Primoy.objects.get(id=pk)
        if p.kanal == k:
            p.delete()
        return Response()


class LikeApiView(APIView):
    def get(self,request):
        k = Kanal.objects.get(user=request.user)
        v = Video.objects.get(kanal=k)
        l = Like.objects.all().like_soni
        ser = LikeSerializers(l,many=True)
        return Response(v,ser.data)
    def post(self,request):
        malumot = request.data
        ser = LikeSerializers(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)

class CommentApiView(APIView):
    def get(self,request):
        k = Kanal.objects.get(user=request.user)
        v = Video.objects.get(kanal=k)
        c = Comment.objects.all(video=v)
        ser = CommentSerializers(c,many=True)
        return Response(ser.data)
    def post(self,request):
        mal= request.data
        ser = CommentSerializers(data=mal)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)



class PlaylistApiView(APIView):
    def get(self,request):
        p = Playlist.objects.all()
        ser = PlaylistSerializers(p,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = PlaylistSerializers(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)

class CommentDel(APIView):
    def delete(self,request,pk):
        k = Kanal.objects.get(user=request.user)
        c = Comment.objects.get(id=pk)
        if c.kanal == k:
            c.delete()
        return Response()
