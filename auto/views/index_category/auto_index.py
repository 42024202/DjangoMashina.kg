from django.views.generic import ListView
from auto.models import CarAnnouncement, MotoAnnouncement
from itertools import chain
from operator import attrgetter


class IndexView(ListView):
    model = CarAnnouncement
    template_name = 'auto/index.html'
    context_object_name = 'cars'
    paginate_by = 20

    def get_queryset(self):
        car_announcements = CarAnnouncement.objects.all()
        moto_announcement = MotoAnnouncement.objects.all()
        combined = sorted(
                chain(car_announcements, moto_announcement), 
                key=attrgetter('created_at'),
                reverse=True
            )
        return combined

