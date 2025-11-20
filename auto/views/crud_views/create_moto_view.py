from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from auto.models import  MotoAnnouncement, MotoAnnouncementImage
from favorites.models import Favorite
from auto.forms import MotoAnnouncementForm, MotoImageForm


class CreateMotoAnnouncementView(LoginRequiredMixin, CreateView):
    model = MotoAnnouncement
    form_class = MotoAnnouncementForm
    template_name = 'auto/create_announcement.html'
    success_url = reverse_lazy('auto:index')

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

