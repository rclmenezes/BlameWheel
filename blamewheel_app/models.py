from django.db import models
from django.contrib.auth.models import User

class BlameWheel(models.Model):
    blamewheel_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="BlamewheelUser")
    name = models.CharField(max_length=200)
    rigged = models.ForeignKey('Blame')

class Blame(models.Model):
    blame_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=6)
    size = models.IntegerField()