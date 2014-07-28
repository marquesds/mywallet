from django.conf.urls import patterns, url

urlpatterns = patterns('mywallet.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^home/$', 'home', name='home'),
    url(r'^bill/(?P<pk>\d+)/$', 'bill', name='bill'),
)
