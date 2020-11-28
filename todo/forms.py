from django import forms
from . models import TodoList

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'end_date')
        widgets = {

            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'end_date': DateInput()
        }