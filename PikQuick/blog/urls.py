from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       )
