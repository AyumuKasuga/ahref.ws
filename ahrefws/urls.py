from django.conf.urls import patterns, include, url
from django.contrib import admin
from ahrefws import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'shorturl.views.main_page', name='main_page'),
    url(r'^add-url/', 'shorturl.views.add_url', name='add_url'),
    url(r'^u/(?P<url>.*)/', 'shorturl.views.follow_url', name='follow_url'),
    url(r'^api/', 'shorturl.views.api_help_page', name='api_help_page'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
)
