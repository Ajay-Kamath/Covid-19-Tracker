from django import forms
from .models import *
from django.forms import ModelForm

class PatientsForm(forms.ModelForm):

    class Meta:
        model = Patients
        fields = '__all__'