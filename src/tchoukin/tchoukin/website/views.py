from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils import simplejson as json
from tchoukin.clubs.forms import ClubForm
from tchoukin.clubs.views import allclubs
from tchoukin.events.forms import EventForm
from tchoukin.events.views import allevents


def initmap(request, where='', template='home.html'):
    clubform = ClubForm
    eventform = EventForm

    return render(request, template, {
        'where': where,
        'clubform': clubform,
        'eventform': eventform
    })


def alldata(request):
    data = (allevents() + allclubs())

    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), mimetype="application/json")
