from django.db import models
from userapp.models import Kanal

class Primoy(models.Model):
    matn = models.TextField()
    koryatkanlar = models.PositiveIntegerField()
    boshlangani = models.TimeField(auto_now_add=True)
    kanal = models.OneToOneField(Kanal,on_delete=models.CASCADE,related_name="kanal_efir")

class Video(models.Model):
    nom = models.CharField(max_length=200)
    koryatkanlar = models.PositiveIntegerField()
    video = models.URLField()
    kanal = models.ForeignKey(Kanal,on_delete=models.CASCADE,related_name="kanal_video",null=True)
    primoy = models.OneToOneField(Primoy, on_delete=models.CASCADE, related_name="efir_video")

class Reccomend(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name="rec_video",)
    kanal = models.ForeignKey(Kanal,on_delete=models.CASCADE,related_name="kanal_rec",)

class Comment(models.Model):
    matn = models.CharField(max_length=200)
    sana = models.DateField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="rec_video")
    kanal = models.ForeignKey(Kanal, on_delete=models.CASCADE, related_name="kanal_rec", )

class Like(models.Model):
    like_soni = models.PositiveIntegerField()
    video = models.ForeignKey(Kanal, on_delete=models.CASCADE, related_name="video_like", null=True)
    kanal = models.ForeignKey(Kanal, on_delete=models.CASCADE, related_name="kanal_like", null=True)


class Playlist(models.Model):
    nom =models.CharField(max_length=200)
    rasim = models.FileField(null=True)
    kanal = models.ForeignKey(Kanal,on_delete=models.CASCADE,related_name="playlist_kanal",null=True)