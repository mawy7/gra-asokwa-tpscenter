from django.contrib import admin
from .models import *



class FinancialAdmin(admin.ModelAdmin):
    list_display = ("account_type", "created_date", "user", "name_of_taxpayer", "recieving_officer")
    list_filter = ("name_of_taxpayer", "time_collected")



admin.site.register(Financial, FinancialAdmin)