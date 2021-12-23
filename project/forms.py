from django.forms import ModelForm
from  .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('id',)
        fields = '__all__'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('id','assigned_to')
        fields = '__all__'
        widgets = {
            'start': DateInput(),
            'end':DateInput()
        }