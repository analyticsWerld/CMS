from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect  
from .forms import AnnouncementForm 
from .models import Announcement
from django.contrib.auth.decorators import login_required



# Create your views here.
#@login_required  
def createAnnouncement(request):  
    if request.method == "POST":  
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            try:  
                form.save()  
                return redirect('show_announcement')  
            except:  
                pass
    else:  
        form = AnnouncementForm()  
    return render(request,'announcement/create.html',{'form':form}) 

#@login_required
def show_Announcement(request):
    announcements = Announcement.objects.all().order_by("deadline") 
    return render(request,"announcement/show.html",{'announcements':announcements})  

#@login_required
def editAnnouncement(request,id): 
    announcements = Announcement.objects.get(id=id) 
    if request.method == "POST":  
        form = AnnouncementForm(request.POST,instance = announcements)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show_announcement')  
            except:  
                pass 
    else:  
        form = AnnouncementForm(instance = announcements)  
    return render(request,'announcement/edit.html',{'form':form}) 


#@login_required
def delete_Announcement(request, id):  
    announcements = Announcement.objects.get(id=id)  
    announcements.delete()  
    return redirect("show_announcement") 

