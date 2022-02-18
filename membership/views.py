from re import template
from django.views.generic import ListView
from django.shortcuts import render, redirect  
from .forms import MemberCreationForm,MemberEditForm
from .models import Member
from django.core.exceptions import PermissionDenied
from django.db.models import Value as V
from django.db.models import Q
from django.db.models.functions import Concat
#from django.contrib.auth.decorators import login_required

list_display = ['Full Name', 'Class', 'Birthday', 'Baptised',"Contact","Address"]
#ids = range(1,len(Member.objects.all()))

#@login_required
def create_member(request):  
    if request.method == "POST":  
        form = MemberCreationForm(request.POST,request.FILES)
        if form.is_valid():
            try:  
                form.save()
                return redirect('show_members')  
            except:  
                pass
    else:  
        form = MemberCreationForm()  
    return render(request,'membership/create.html',{'form':form}) 

#@login_required
def show_members(request):
     members = Member.objects.order_by('id') 
     return render(request,"membership/show_members.html",{'members':members,"display":list_display})  

#@login_required
def show_member(request, id):
     member = Member.objects.get(id=id)
     return render(request,"membership/show_member.html",{'member':member})  



#@login_required
def edit_member(request,id): 
     member = Member.objects.get(id=id) 
     if request.method == "POST":  
         form = MemberEditForm(request.POST,request.FILES,instance = member)  
         if form.is_valid():
             print("form is valid")  
             try:  
                 form.save()  
                 return redirect('show_members')  
             except:  
                return render(request,'membership/edit.html',{'form':form}) 
     else:  
         form = MemberCreationForm(instance = member)  
     return render(request,'membership/edit.html',{'form':form}) 

def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('q', None)
        if search_query:
            print(search_query)
            if len(search_query.split()) == 1:
                results = Member.objects.filter( Q(first_name__icontains = search_query) | Q(last_name__icontains = search_query))
            else:
                for name in search_query.split():
                    results = Member.objects.annotate(fullname = Concat('first_name', V(' '),'last_name')).filter( Q(first_name__icontains = name))
                    print(results)
            return render(request,'membership/search_results.html',{'results':results,"query":search_query})



#@login_required
def delete_member(request, id):  
    member = Member.objects.get(id=id) 
    # if member.is_superuser or member.is_staff:
    raise PermissionDenied
    pass
    # else: 
    #     member.delete()  
    return redirect("show_members") 

