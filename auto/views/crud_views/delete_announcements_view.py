from django.apps import apps
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class DeleteAnnouncementView(LoginRequiredMixin, DeleteView):
    """Universal view for deleting car and moto announcements."""
    template_name = 'auto/delete_confirmation.html'
    success_url = reverse_lazy('auto:get_my_announcements')

    def dispatch(self, request, *args, **kwargs):
            model_name = kwargs["model_name"].lower()
            pk = kwargs["pk"]

            self.model = apps.get_model("auto", model_name)
            self.object = get_object_or_404(self.model, pk=pk)

            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
            return reverse_lazy("favorites:get_my_announcements")

