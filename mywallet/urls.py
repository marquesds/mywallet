from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('mywallet.core.urls', namespace='core')),
    url(r'^accounts/', include('mywallet.accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
)
