from django.shortcuts import render, redirect  
from .forms import FinanceForm 
from .models import Finance
from django.contrib.auth.decorators import login_required


# Create your views here.  
#@login_required(login_url="apps_login")
def createFinance(request):  
    if request.method == "POST":  
        form = FinanceForm(request.POST)  
        if form.is_valid():  
            print('form is valid')
            
            try:  
                form.save() 
                print('form is saved') 
                return redirect('show_finance') 
                
            except:  
                print('form is not saved')
                pass 
        else:
            print('form is not valid') 
    else:  
        form = FinanceForm()  
    return render(request,'finance/create.html',{'form':form}) 


#@login_required(login_url="apps_login")
def show_Finance(request):
    finances = Finance.objects.all() 
    return render(request,"finance/show.html",{'finances':finances})  


#@login_required(login_url="apps_login")
def editFinance(request,id): 
    finances = Finance.objects.get(id=id) 
    if request.method == "POST":  
        form = FinanceForm(request.POST,instance = finances)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show_finance')  
            except:  
                pass  
    else:  
        form = FinanceForm(instance = finances)  
    return render(request,'finance/edit.html',{'form':form}) 


#@login_required(login_url="apps_login")
def delete_Finance(request, id):  
    finances = Finance.objects.get(id=id)  
    finances.delete()  
    return redirect("show_finance") 

