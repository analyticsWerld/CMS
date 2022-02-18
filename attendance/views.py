from django.shortcuts import render, redirect  
from .forms import AttendanceForm 
from .models import Attendance
from django.contrib.auth.decorators import login_required
from membership.models import Member



#@login_required(login_url="apps_login") 
def attendance(request):
    members = Member.objects.order_by('last_name')

    if request.method == "POST":  
        fil = request.POST.get("filter")
        print("hi")
        if form.is_valid():
            print("form is valid")
            try:  
                form.save()  
                return redirect('show_attendance')  
            except:  
                pass
        else:
            print("form is not valid")  
    else:  
        form = AttendanceForm()  
    return render(request,'attendance/create.html',{'members':members}) 

#@login_required(login_url="apps_login")
# def show_attendance(request):
#     attendance = Attendance.objects.all().order_by("deadline") 
#     return render(request,"attendance/show.html",{'attendance':attendance})  

# #@login_required(login_url="apps_login")
# def edit_attendance(request,id): 
#     attendance = Attendance.objects.get(id=id) 
#     if request.method == "POST":  
#         form = AttendanceForm(request.POST,instance = attendance)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('show_attendance')  
#             except:  
#                 pass 
#     else:  
#         form = AttendanceForm(instance = attendance)  
#     return render(request,'attendance/edit.html',{'form':form}) 


# #@login_required(login_url="apps_login")
# def delete_attendance(request, id):  
#     attendance = Attendance.objects.get(id=id)  
#     attendance.delete()  
#     return redirect("show_attendance") 

