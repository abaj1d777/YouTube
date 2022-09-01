from django.contrib.auth.models import User
from .models import *
from userapp.models import Kanal
from rest_framework import serializers



class ReccommendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reccomend
        fields="__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields="__all__"

class PrimoySerializers(serializers.ModelSerializer):
    class Meta:
        model=Primoy
        fields="__all__"


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields="__all__"

class KanalSerializers(serializers.ModelSerializer):
    class Meta:
        model=Kanal
        fields="__all__"

class PlaylistSerializers(serializers.ModelSerializer):
    class Meta:
        model=Playlist
        fields="__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"