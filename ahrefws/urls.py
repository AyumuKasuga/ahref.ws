from django.conf.urls import patterns, include, url
from django.contrib import admin
from ahrefws import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ahrefws.views.home', name='home'),
    # url(r'^ahrefws/', include('ahrefws.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'shorturl.views.main_page', name='main_page'),
    url(r'^add-url/', 'shorturl.views.add_url', name='add_url'),
    url(r'^u/(?P<url>.*)/', 'shorturl.views.follow_url', name='follow_url'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
)
