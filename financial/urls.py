from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from financial import views
from financial.views import FinancialViewsSets

app_name = 'financial'
router = routers.DefaultRouter()
router.register(r'financial', FinancialViewsSets)

urlpatterns = [
    path('ent', view=views.entry, name='entry'),
    path('entries', view=views.entries, name='entries'),
    path('submit_financial', login_required(views.submit_financial), name='submit_financial'),
    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    
]