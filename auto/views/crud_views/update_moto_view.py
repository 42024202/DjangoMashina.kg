from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from auto.models import MotoAnnouncement, MotoAnnouncementImage
from auto.forms import MotoAnnouncementForm
