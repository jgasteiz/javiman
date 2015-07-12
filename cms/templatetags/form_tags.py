from django import template
from django import forms
register = template.Library()


@register.filter(name='add_css_class')
def add_css_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__ == forms.CheckboxInput
