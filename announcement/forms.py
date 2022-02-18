from django import forms
from .models import Announcement
from django.utils import timezone



class AnnouncementForm(forms.ModelForm):

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline is not None and deadline < timezone.now():
            raise forms.ValidationError("The date cannot be in the past!")
        return deadline
    
    class Meta:
        model = Announcement
        exclude = ('date_reg',)
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        


