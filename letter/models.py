from django.db import models
from django.shortcuts import render
import datetime
from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone


class Letter(models.Model):
    created_date = models.DateField(default=date.today, blank=True, null=True)
    name_of_taxpayer = models.CharField(max_length=80, default="")
    upload_document = models.FileField(upload_to='documents/')
    recieving_officer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='letter_officer_recieving_files', on_delete=models.CASCADE)
    time_collected = models.DateField(default=date.today, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Letter", default='', on_delete=models.CASCADE)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.name_of_taxpayer)
