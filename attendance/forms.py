from django import forms
from .models import Attendance
import datetime


class AttendanceForm(forms.ModelForm):
        
    class Meta:
        model = Attendance
        exclude = ("",)
        


