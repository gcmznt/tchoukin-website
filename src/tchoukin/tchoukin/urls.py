from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskdown.views.home', name='home'),
    # url(r'^taskdown/', include('taskdown.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^clubs/', include('tchoukin.clubs.urls')),
    url(r'^events/', include('tchoukin.events.urls')),
    url(r'^', include('tchoukin.website.urls')),
)
