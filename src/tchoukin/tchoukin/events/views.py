import uuid
import socket
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from datetime import datetime
from tchoukin.events.models import Event
from tchoukin.events.forms import EventForm
import twitter


def get_field(f):
    if hasattr(f, 'pk'):
        return f.pk

    return f


def confirmevent(request, code=''):
    try:
        instance = Event.objects.get(confirmation_code=code)
        instance.status = 'confirmed'
        instance.confirmation_code = ''
        instance.save()

        # api = twitter.Api(consumer_key='RQWOMjnOvzLetMsueVDhuQ', consumer_secret='WjVr9yjaz80oXIcRQUdM0gKKqqbiXSyiTFsgWtbPg', access_token_key='1024412977-nw6ecEQpl3U9ECuwCpj2nNKrJNsJhROzzbV3Zov', access_token_secret='TpSlRJwhFgPxHwwY3YBpUdkrXGikSQ0H2r6nfHBHSIQ')
        # api.PostUpdates('Wellcome on TchoukIN ' + instance.name)
    except:
        pass

    return redirect('website_home')


def saveevent(request):
    response = {}

    confirmation_code = uuid.uuid1().hex
    form_cls = EventForm
    partial = Event(ip_address=request.META['REMOTE_ADDR'], status='pending', confirmation_code=confirmation_code)

    if request.method == 'POST':

        form = form_cls(request.POST, request.FILES, instance=partial)
        if form.is_valid():
            # print "Saving..."
            newevent = form.save()
            send_mail('Confirm your TchoukPoint', 'To confirm your TchoukPoint go to this URL: http://' + request.get_host() + '/events/confirm/' + confirmation_code, 'noreply@tchouk.in', [newevent.email], fail_silently=False)

            response['status'] = 'ok'
        else:
            response['status'] = 'ko'
            response['errors'] = form.errors

        return HttpResponse(json.dumps(response), mimetype="application/json")

    return HttpResponse('')


def allevents():
    model_fields = ['name', 'website', 'email', 'from_date', 'to_date', 'address_lat', 'address_lon']
    events = []
    for instance in Event.objects.filter(status='confirmed', to_date__gte=datetime.now()):
        row = dict((f, get_field(getattr(instance, f))) for f in model_fields)
        row['type'] = 'event'
        events.append(row)

    return events
