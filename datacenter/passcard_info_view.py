from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def format_duration(duration):
    hours, minutes, seconds = duration // 3600, duration // 60 % 60, duration % 60
    if hours:
        return f'{hours:d}:{minutes:02d}:{seconds:02d}'
    return f'{minutes:d}:{seconds:02d}'


def get_visit_dict(visit):
    return {
        'entered_at': visit.entered_at,
        'duration': format_duration(visit.get_duration()),
        'is_strange': visit.is_visit_long()
    }


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = [
        get_visit_dict(visit) for visit in Visit.objects.filter(passcard=passcard)
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
