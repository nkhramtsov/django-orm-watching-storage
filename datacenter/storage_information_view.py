from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now
from utils import format_duration


def get_visit_dict(visit):
    return {
        'who_entered': visit.passcard.owner_name,
        'entered_at': visit.entered_at,
        'duration': format_duration(visit.get_duration()),
    }


def storage_information_view(request):
    non_closed_visits = [
        get_visit_dict(visit) for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
