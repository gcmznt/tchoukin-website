from django.shortcuts import render
from tchoukin.clubs.forms import ClubForm
from tchoukin.clubs.models import Club


def initmap(request, where='', template='home.html'):
    instance = Club()
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            # print "Saving..."
            instance = form.save()
    else:
        form = ClubForm

    return render(request, template, {
        'where': where,
        'clubform': form
    })
