from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Recipient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    phone_number = models.CharField(max_length=100, verbose_name="Телефон")

    def __str__(self):
        return self.name + ' : ' + self.phone_number
