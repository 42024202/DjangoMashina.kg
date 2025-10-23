from django import template

register = template.Library()

@register.filter
def add_placeholder(field, placeholder_text=None):
    placeholder = placeholder_text or field.label
    return field.as_widget(attrs={"placeholder": placeholder, "class": "form-control"})

