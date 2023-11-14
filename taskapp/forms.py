from .models import Task
from django import forms

"""class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'text', 'completado']"""

class TaskForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    text = forms.CharField(label="text", widget=forms.Textarea)
    completado = forms.BooleanField(label="completado", required=False)