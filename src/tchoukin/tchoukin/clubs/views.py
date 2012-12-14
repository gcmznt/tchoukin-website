from django.shortcuts import render
from django.utils import simplejson as json
from django.http import HttpResponse
from tchoukin.clubs.models import Club


def get_field(f):
    if hasattr(f, 'pk'):
        return f.pk

    return f


def allclubs(request):
    model_fields = [f.name for f in Club._meta._fields()]
    clubs = []
    for instance in Club.objects.all():
        row = {f: get_field(getattr(instance, f)) for f in model_fields}
        clubs.append(row)

    return HttpResponse(json.dumps(clubs), mimetype="application/json")
