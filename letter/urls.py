from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from letter import views
from letter.views import LetterViewsSets

app_name = 'letter'
router = routers.DefaultRouter()
router.register(r'letter', LetterViewsSets)

urlpatterns = [
    path('ent', view=views.entry, name='entry'),
    path('entries', view=views.entries, name='entries'),
    path('submit_letter', login_required(views.submit_letter), name='submit_letter'),
    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    
]