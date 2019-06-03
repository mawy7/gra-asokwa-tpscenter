from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from tcc import views
from tcc.views import TccViewsSets

app_name = 'tcc'
router = routers.DefaultRouter()
router.register(r'tcc', TccViewsSets)

urlpatterns = [
    path('ent', view=views.entry, name='entry'),
    path('entries', view=views.entries, name='entries'),
    path('submit_tcc', login_required(views.submit_tcc), name='submit_tcc'),
    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    
]