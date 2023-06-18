from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit.get_duration(visit)),
            'is_strange': visit.is_visit_long(visit)
        }
        for visit in Visit.objects.filter(leaved_at=None)
        ]

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
