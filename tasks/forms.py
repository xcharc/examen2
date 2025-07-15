from django import forms
from .models import PendingTask
class PendingTaskForm(forms.ModelForm):
    class Meta:
        model = PendingTask
        fields = ['api_id', 'user_id', 'title', 'completed']