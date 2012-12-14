from django.conf.urls import patterns, url
from tchoukin.clubs.views import allclubs

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', allclubs, name="clubs_list"),
)
