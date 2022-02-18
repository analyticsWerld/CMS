from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MemberCreationForm,MemberEditForm

from .models import Member

class MemberAdmin(UserAdmin):
    model = Member
   
    list_display = ['username', 'first_name', 'last_name', 'is_staff']
    #fieldsets = UserAdmin.fieldsets + (
    #        (None, {'fields': ('mobile_number', 'birth_date')}),
    #)

admin.site.register(Member, MemberAdmin)
