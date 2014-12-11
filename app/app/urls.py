from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from site_2015.models import Page, Home

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'site_2015.views.home'),
    url(r'^(?P<slug>[\w\-]+)/$', 'site_2015.views.page'),
)
