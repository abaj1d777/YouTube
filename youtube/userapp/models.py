from django.contrib.auth.models import User
from django.db import models

class Kanal(models.Model):
    nomi = models.CharField(max_length=200)
    rasm = models.FileField(null=True)
    following = models.PositiveIntegerField()
    follower = models.PositiveIntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
