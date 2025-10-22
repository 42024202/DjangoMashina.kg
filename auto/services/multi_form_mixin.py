from django.views.generic.edit import CreateView
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


 
