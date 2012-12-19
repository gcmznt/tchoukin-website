from django.shortcuts import render, redirect
from django.utils import simplejson as json
from django.http import HttpResponse
from tchoukin.clubs.models import Club
from tchoukin.clubs.forms import ClubForm


def get_field(f):
    if hasattr(f, 'pk'):
        return f.pk

    return f


def confirmclub(request, code=''):
    try:
        instance = Club.objects.get(confirmation_code=code)
        instance.status = 'confirmed'
        instance.confirmation_code = ''
        instance.save()
    except:
        pass

    return redirect('website_home')


def saveclub(request):
    response = {}
    instance = Club()
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            # print "Saving..."
            instance = form.save()
            response['status'] = 'ok'
        else:
            response['status'] = 'ko'
            response['errors'] = form.errors

        return HttpResponse(json.dumps(response), mimetype="application/json")

    return HttpResponse('')


def allclubs(request):
    model_fields = ['name', 'website', 'email', 'address_lat', 'address_lon']
    clubs = []
    for instance in Club.objects.filter(status='confirmed'):
        row = dict((f, get_field(getattr(instance, f))) for f in model_fields)
        clubs.append(row)

    return HttpResponse('var data = {"clubs": ' + json.dumps(clubs) + '}', mimetype="application/json")
