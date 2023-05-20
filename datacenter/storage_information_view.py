from datacenter.models import Visit
from django.shortcuts import render
from .visit_duration_operations import * 

def storage_information_view(request):
    non_closed_visits = []
    for passcard in Visit.objects.filter(leaved_at__isnull=True):
        duration = get_visit_duration(passcard)
        visitor_name = passcard.passcard.owner_name
        entered_time = passcard.entered_at
        visit_duration = format_duration(duration)
        non_closed_visits.append(
            {
                'who_entered': visitor_name,
                'entered_at': entered_time,
                'duration': visit_duration,
                'is_strange': is_visit_long(passcard)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
