from django.conf.urls import patterns, url

urlpatterns = patterns('mywallet.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^home/$', 'home', name='home'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^donate/$', 'donate', name='donate'),
    url(r'^bill/(?P<pk>\d+)/$', 'bill', name='bill'),
)
