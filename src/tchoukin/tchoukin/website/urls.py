from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template
from tchoukin.website.views import initmap, alldata

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^data/$', alldata, name="alldata"),
    url(r'^(?P<where>.*)/$', initmap, {'template': 'mappa.html'}, name="website_home_localized"),
    url(r'^$', initmap, {'template': 'mappa.html'}, name="website_home"),
)
