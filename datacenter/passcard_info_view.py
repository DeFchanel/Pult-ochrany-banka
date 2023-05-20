from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .visit_duration_operations import * 


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for passcard in Visit.objects.filter(passcard=passcard):
        duration = get_visit_duration(passcard)
        entered_time = passcard.entered_at
        visit_duration = format_duration(duration)
        is_strange = is_visit_long(passcard)
        this_passcard_visits.append(
            {
                'entered_at': entered_time,
                'duration': visit_duration,
                'is_strange': is_strange
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
