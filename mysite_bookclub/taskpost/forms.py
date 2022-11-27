from django import forms
from  .models import TaskPost

class TaskPostForm(forms.ModelForm):
    class Meta:
        model = TaskPost
        fields = ('sender', 'description')
