from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now


def format_duration(duration):
    hours, minutes, seconds = duration // 3600, duration // 60 % 60, duration % 60
    if hours:
        return f'{hours:d}:{minutes:02d}:{seconds:02d}'
    return f'{minutes:d}:{seconds:02d}'


def get_visit_dict(visit):
    return {
        'who_entered': visit.passcard.owner_name,
        'entered_at': visit.entered_at,
        'duration': format_duration(visit.get_duration()),
    }


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = [
        get_visit_dict(visit) for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
