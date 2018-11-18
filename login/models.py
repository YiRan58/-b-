from django.db import models

# Create your models here.


class Users(models.Model):
    userTel = models.CharField(primary_key=True, max_length=12)
    userName = models.CharField(max_length=16)
    userMail = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=20)


class Cs(models.Model):
    csId = models.IntegerField(primary_key=True)
    csAdd = models.CharField(max_length=50)
    csStates = models.BooleanField()
    csFreeTime = models.TimeField


class UserCs(models.Model):
    userTel = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    csId = models.ForeignKey(Cs, on_delete=models.DO_NOTHING)
