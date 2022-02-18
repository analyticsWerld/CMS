from django import forms
from django.contrib.auth.forms import UsernameField,UserCreationForm,AuthenticationForm,UserChangeForm
from django.forms.widgets import PasswordInput
from .models import Member
from django.utils import timezone
import random




class MemberCreationForm(UserCreationForm):
    password = forms.CharField(required=False,widget=PasswordInput)
    password1 = forms.CharField(required = False,widget=PasswordInput)
    password2 = forms.CharField(required = False,widget=PasswordInput)
    username = UsernameField(required=False)
    class Meta:
        model = Member
        exclude = ("id","last_login","is_superuser","is_staff","is_active","date_joined","groups","user_permissions")
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'date_joined_church': forms.DateInput(attrs={'type': 'date'}),
            'photo' : forms.ClearableFileInput(attrs={'type':'file','accept':'image/*', 'onchange':"readURL(this)"})
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username or username == "":
             number = '{:03d}'.format(random.randrange(1, 999))
             username = ("COC" + number)
             while Member.objects.filter(username = username):
                 number = '{:03d}'.format(random.randrange(1, 999))
                 username = ("COC" + number)
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if (password1 and password2): 
            if(password1 != password2):
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        else:
            print(self.cleaned_data.get("first_name"))
            first_letter = self.cleaned_data.get("first_name")[:3]
            three_letters_surname = self.cleaned_data.get("last_name")[:3]
            number = '{:03d}'.format(random.randrange(1, 999))
            password2 = (first_letter + three_letters_surname + number)
            password1 = password2
        
       
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email or email != "":
            if Member.objects.filter(email = email):
                raise forms.ValidationError('Email is already in use.')
        return email

    # def clean_mobile_number(self):
    #     mobile_number = self.cleaned_data.get("mobile_number")
    #     if not mobile_number or mobile_number != "":
    #         if Member.objects.filter(mobile_number = mobile_number):
    #             raise forms.ValidationError('User with same mobile number already exist.')
    #     return mobile_number

    
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date is not None and birth_date > timezone.now().date():
            raise forms.ValidationError("The birthday cannot be in the future!")
        return birth_date
    

    def clean_date_joined_church(self):
        date_joined_church = self.cleaned_data.get('date_joined_church')
        if date_joined_church is not None and date_joined_church > timezone.now().date():
            raise forms.ValidationError("The birthday cannot be in the future!")
        return date_joined_church

    


        
class MemberEditForm(UserChangeForm):
    
    class Meta:
        model = Member
        exclude = ("id","username","password","date_joined","is_staff","is_superuser","is_active")
        widgets = {
             'photo' : forms.ClearableFileInput(attrs={'type':'file','accept':'image/*', 'onchange':"readURL(this)"})
         }


        


class LoginForm(AuthenticationForm):
    

    class Meta:
        fields = ("username","password")
        widgets = {
             'username': forms.TextInput(attrs={'placeholder': 'Username'}),
             'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
         }

