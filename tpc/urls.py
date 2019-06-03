from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home import views
from letter.views import *
from financial.views import *
from turnover.views import *



urlpatterns = [
	path('', include('home.urls', namespace='home')),
    path('accounts/', include('registration.backends.default.urls')),
    #path('accounts/', include('registration.backends.simple.urls')),
    path('profile/', include('registration.urls', namespace='profiles')),
    path('financial/', include('financial.urls', namespace='financial')),
    path('letter/', include('letter.urls', namespace='letter')),
    path('turnover/', include('turnover.urls', namespace='turnover')),
    path('tcc/', include('tcc.urls', namespace='tcc')),
   path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.

handler404 = 'home.views.handler404'



