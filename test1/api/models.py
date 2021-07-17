from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=32, blank=False, null=False, unique=True)
    password = models.CharField(max_length=128, blank=False, null=False)


class UserInfo(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    age = models.IntegerField(max_length=3, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
