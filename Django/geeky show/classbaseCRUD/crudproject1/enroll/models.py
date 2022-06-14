from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=100)
