from django import forms
from tasks.models import tasks_snippet


class task_snippet_form(forms.ModelForm):
    
    class Meta:
        model = tasks_snippet
        fields = ('task_details','due_date') 

    