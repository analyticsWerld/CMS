from django.shortcuts import render,redirect
from membership.forms import LoginForm
from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from membership.analytics import member_summary_context

context = {}
context.update(member_summary_context)
def viewbase(request):
    return render(request, "cms/baseApp.html")

def home(request):
    return render(request, "cms/index.html")

#@login_required(login_url="apps_login")
def apps(request):
    return render(request, "cms/apps.html")

def dashboard(request):

    return render(request, "cms/dashboard.html",context)
  

#@user_passes_test(lambda u: u.is_staff)
def apps_login(request):
    if request.method == "POST":  
        form = LoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            try:
                user = form.get_user()
                login(user)
                redirect("apps")
            except:  
                return render(request,"cms/login.html")
    else:  
        form = LoginForm()  
    return render(request,'cms/login.html',{'form':form})


        
