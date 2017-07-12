# models.py
from django.db import models


class usertable(models.Model):
    userid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class hosttable(models.Model):
    hostid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=50)
    hostip = models.GenericIPAddressField()
    hostcpu = models.CharField(max_length=50)
    hostmem = models.CharField(max_length=10)
    hosthdd = models.CharField(max_length=10)