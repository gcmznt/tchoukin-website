from django.shortcuts import render
from tchoukin.clubs.forms import ClubForm


def initmap(request, where='', template='home.html'):
    form = ClubForm

    return render(request, template, {
        'where': where,
        'clubform': form
    })
