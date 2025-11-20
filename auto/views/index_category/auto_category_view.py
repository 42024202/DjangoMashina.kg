from django.views.generic import ListView
from auto.models import CarAnnouncement
from auto.filters import CarAnnouncementFilter


class CategoryView(ListView):
    template_name = 'auto/category.html'
    context_object_name = 'cars'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        queryset = CarAnnouncement.objects.filter(category__name=category_name)
        self.car_filter = CarAnnouncementFilter(self.request.GET, queryset=queryset)
        return self.car_filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.car_filter
        context['category_name'] = self.kwargs['category_name']
        #context['categories'] = Category.objects.all(parent__isnull=True)
        return context

