from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Equip_Classify(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Laboratory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    lab_ID = models.CharField(max_length=50)
    lab_deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    classify = models.ForeignKey(Equip_Classify, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    assigned_lab = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    task_done = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

