from django import forms
from .models import *
from django.forms.models import inlineformset_factory

ModuleFormSet = inlineformset_factory(Course,
                                     Module,
                                     fields=['title','description'],
                                     extra=2,
                                     can_delete=True)