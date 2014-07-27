from django.conf.urls import patterns, url

urlpatterns = patterns('mywallet.core.views',
    url(r'^$', 'home', name='home'),
)
