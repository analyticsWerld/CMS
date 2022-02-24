from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from datetime import date



class_options = [("ADULT","Adult"), ("CHILDREN","Children"), ("YOUTH", "Youth"), ("NEW CONVERT","New Convert")]
role_options = [("ELDER", "Elder"),("DEACON", "Deacon"),("PREACHER","Preacher"),("SECRETARY", "Secretary")]
gender_options = [("MALE","Male"),("FEMALE","Female")]
baptism = [("YES","Yes"),("NO","No")]
# Create your models here.
class MemberUserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        #TODO : Modify this to prevent superuser status from being nullified
        
        extra_fields["is_staff"] =  False
        extra_fields["is_superuser"] =  False
            
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(username, password, **extra_fields)


class Member(AbstractUser):

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [] 
    birth_date = models.DateField(blank=True,null=True )
    date_joined_church = models.DateField(blank=True,null=True )
    photo = models.ImageField(upload_to='members/%Y',blank=True)
    church_role = models.CharField(choices=role_options, max_length=250,blank=True)
    church_class = models.CharField(choices=class_options, max_length=250)
    address = models.TextField(max_length=250,blank=True,null=True)
    gender = models.CharField(choices=gender_options, max_length=250 )
    mobile_number = models.CharField(max_length=15,blank=True,null=True)
    occupation = models.CharField(max_length=250,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    baptised = models.CharField(blank=True, null=True,choices=baptism,max_length=5)

    objects = MemberUserManager()
    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def get_generic_name(self):
        if str.lower(self.church_role) == "elder":
            title = "Eld."
        elif str.lower(self.church_role) == "deacon":
            title = "Deac."
        else:
            if str.lower(self.church_class) == "children":
                title = ""
            else:
                if str.lower(self.gender) == "male":
                    title = "Bro."
                else:
                    if self.age > 35:
                        title = "Mad."
                    else:
                        title = "Sis."


        generic_name = title + " " + self.first_name + " " + self.last_name.split()[-1] 
        return generic_name

    @property
    def age(self):
        today = date.today()
        if self.birth_date:
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        else:
            age = 0
        print(age)
        return age




    def __str__(self):
        return f'Profile for user {self.username}'

    
    




