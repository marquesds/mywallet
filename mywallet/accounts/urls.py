from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'accounts:login'}, name='logout'),
    url(r'^signup/$', 'mywallet.accounts.views.signup', name='signup'),
    url(r'^preferences/$', 'mywallet.accounts.views.preferences', name='preferences'),
)