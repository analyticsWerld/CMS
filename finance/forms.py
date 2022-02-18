from django import forms
from .models import Finance
import datetime


class FinanceForm(forms.ModelForm):
        
    class Meta:
        model = Finance
        fields = ('describe','amount','did_by','type_of')
        


