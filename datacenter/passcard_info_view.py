from django.shortcuts import get_object_or_404, render

from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit.get_duration(visit)),
            'is_strange': visit.is_visit_long(visit)
        } for visit in Visit.objects.filter(passcard__passcode=passcode)]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
