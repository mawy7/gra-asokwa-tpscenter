from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from turnover import views
from turnover.views import TurnoverViewsSets

app_name = 'turnover'
router = routers.DefaultRouter()
router.register(r'turnover', TurnoverViewsSets)

urlpatterns = [
    path('ent', view=views.entry, name='entry'),
    path('entries', view=views.entries, name='entries'),
    path('submit_turnover', login_required(views.submit_turnover), name='submit_turnover'),
    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    
]