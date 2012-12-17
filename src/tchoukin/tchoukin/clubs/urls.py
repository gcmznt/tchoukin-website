from django.conf.urls import patterns, url
from tchoukin.clubs.views import allclubs, saveclub, confirmclub

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^confirm/(?P<code>.*)/$', confirmclub, name="confirm_club"),
    url(r'^save/$', saveclub, name="save_club"),
    url(r'^$', allclubs, name="clubs_list"),
)
