# models.py
from django.db import models


class usertable(models.Model):
    userid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)