from django import forms
from .models import Task

class TaskForm(forms.ModelForm): 
    my_status = [
        ('pending', 'Pending'), #responsible for the drop down in the form
        ('completed', 'Completed'),
    ]
    status = forms.ChoiceField(choices=my_status, required=False)   #status is not required because it defaulted to pending.
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']