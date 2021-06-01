from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.subject} + {self.type}'
