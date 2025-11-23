from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseListView(ListView):
    paginate_by = 20
    ordering = '-created_at'


class BaseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'auto/create_announcement.html'
    success_url = None

    image_field_name = 'images'
    image_model = None
    image_fk_field = None

    def form_valid(self, form):
        form.instance.profile = self.request.user
        response = super().form_valid(form)

        images = self.request.FILES.getlist(self.image_field_name)
        for image in images:
            self.image_model.objects.create(
                **{self.image_fk_field: self.object},
                image=image
            )
        return response


class BaseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'auto/create_announcement.html'


class BaseDetailView(DetailView):
    template_name = 'auto/detail.html'
