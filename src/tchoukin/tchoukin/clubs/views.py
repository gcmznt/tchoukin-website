import uuid
import socket
from django.core.mail import send_mail
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

    confirmation_code = uuid.uuid1().hex
    form_cls = ClubForm
    partial = Club(ip_address=request.META['REMOTE_ADDR'], status='pending', confirmation_code=confirmation_code)

    if request.method == 'POST':

        form = form_cls(request.POST, request.FILES, instance=partial)
        if form.is_valid():
            # print "Saving..."
            newclub = form.save()
            send_mail('Confirm your place', 'To confirm your place go to this URL: http://' + request.get_host() + '/clubs/confirm/' + confirmation_code, 'noreply@tchouk.in', [newclub.email], fail_silently=False)

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
