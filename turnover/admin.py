from django.contrib import admin
from .models import  Turnover



class TurnoverAdmin(admin.ModelAdmin):
    list_display = ("created_date", "user", "name_of_taxpayer", "recieving_officer")
    list_filter = ("name_of_taxpayer", "time_collected")


admin.site.register(Turnover, TurnoverAdmin)