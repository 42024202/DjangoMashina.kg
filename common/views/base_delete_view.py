from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404
from django.apps import apps
from django.urls import reverse_lazy


class BaseDeleteAnnouncementView(LoginRequiredMixin, DeleteView):
    """
    Universal delete view by model_name и pk.
    work in all apps.
    """
    template_name = 'auto/delete_confirmation.html'
    app_name = "auto"
    success_url = reverse_lazy('auto:get_my_announcements')

    model = None

    def dispatch(self, request, *args, **kwargs):
        model_name = kwargs.get("model_name").lower()
        pk = kwargs.get("pk")

        """get model by name"""
        self.model = apps.get_model(self.app_name, model_name)
        self.object = get_object_or_404(self.model, pk=pk)

        """check if user is owner"""
        if request.user != self.object.profile:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

