from django.views.generic.edit import CreateView, UpdateView
from ..models import CarImage
from django.shortcuts import render, redirect


class MultiFormCreateView(CreateView):
    """
    Extended CreateView supporting multiple forms,
    expect atribute form_classes
    """
    form_classes = {}
    prefixes = {}
    success_url = None

    def get_forms(self):
        """initializate all forms"""
        forms = {}
        for key, form_class in self.form_classes.items():
            prefix = self.prefixes.get(key)
            if self.request.method == "POST":
                forms[key] = form_class(self.request.POST, self.request.FILES, prefix=prefix)
            else:
                forms[key] = form_class(prefix=prefix)
        return forms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'forms' not in kwargs:
            context['forms'] = getattr(self, 'forms', self.get_forms())
        else:
            context['forms'] = kwargs['forms']
        return context

    def post(self, request, *args, **kwargs):
        self.forms = self.get_forms()
        if all(form.is_valid() for form in self.forms.values()):
            return self.forms_valid(self.forms)
        return self.forms_invalid(self.forms)

    def forms_valid(self, forms):
        raise NotImplementedError("You must implement forms_valid()")

    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))


 
class MulriFormUpdateView(MultiFormCreateView ,UpdateView):
    """Extended UpdateView supporting multiple forms"""
    def get_forms(self):
        """initializate all forms"""
        forms = {}
        for key, form_class in self.form_classes.items():
            prefix = self.prefixes.get(key)

            if key == 'announcement':
                instance = self.get_object()
            elif key == 'config':
                instance = self.get_object().car_config
            else:
                instance = None

            if self.request.method == "POST":
                forms[key] = form_class(
                    self.request.POST,
                    self.request.FILES,
                    instance=instance,
                    prefix=prefix
                )
            else:
                forms[key] = form_class(instance=instance, prefix=prefix)
        return forms

    def post(self, request, *args, **kwargs):
        """Обработка POST-запроса"""
        self.object = self.get_object()
        self.forms = self.get_forms()
        if all(form.is_valid() for form in self.forms.values()):
            return self.forms_valid(self.forms)
        return self.forms_invalid(self.forms)

    def forms_valid(self, forms):
        """Что делать, если все формы валидны"""
        announcement_form = forms['announcement']
        config_form = forms['config']

        car_config = config_form.save()
        car_announcement = announcement_form.save(commit=False)
        car_announcement.car_config = car_config
        car_announcement.save()

        for img in self.request.FILES.getlist('images'):
            CarImage.objects.create(announcement=car_announcement, image=img)

        return redirect(self.success_url)

