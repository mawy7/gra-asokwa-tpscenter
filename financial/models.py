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



class Financial(models.Model):
    ACCOUNT = (('', ''),
                ('LTD', 'Limited'),
              ('ENT', 'Enterprise'),)
    created_date = models.DateField(default=date.today, blank=True, null=True)
    account_type = models.CharField(choices=ACCOUNT, max_length=3, default='')
    created_date = models.DateField(default=date.today, blank=True, null=True)
    name_of_taxpayer = models.CharField(max_length=80, default="")
    tin = models.CharField(max_length=15)
    year = models.PositiveIntegerField(default="2019", blank=True, null=True)
    location_of_business = models.CharField(max_length=52)
    contact_number = models.CharField(max_length=16, blank=False, null=True)
    upload_document = models.FileField(upload_to='documents/')
    recieving_officer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='entry_officer_recieving_files', on_delete=models.CASCADE)
    time_collected = models.DateField(default=date.today, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Financial", default='', on_delete=models.CASCADE)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.created_date)
