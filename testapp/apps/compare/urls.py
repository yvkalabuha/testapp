from django import views

from django.contrib.auth.views import logout
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'testapp.apps.compare.views.index', name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)