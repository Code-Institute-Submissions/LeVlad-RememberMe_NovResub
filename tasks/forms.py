from django import forms
from django.forms import TextInput
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'location', 'priority', 'done')
        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
}