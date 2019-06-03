from django.contrib import admin
from .models import Tcc



class TccAdmin(admin.ModelAdmin):
    list_display = ("created_date", "user", "name_of_company", "recieving_officer")
    list_filter = ("name_of_company", "time_collected")


admin.site.register(Tcc, TccAdmin)