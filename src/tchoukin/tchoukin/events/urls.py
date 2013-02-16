from django.conf.urls import patterns, url
from tchoukin.events.views import allevents, saveevent, confirmevent

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^confirm/(?P<code>.*)/$', confirmevent, name="confirm_event"),
    url(r'^save/$', saveevent, name="save_event"),
)
