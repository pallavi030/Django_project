from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Details

# Create your views here.
def emp_home(request):
    # return HttpResponse("Student home page")
    return render(request,"emp/home.html",{})


def add_emp(request):
    if request.method=='POST':
        
        return redirect("/emp/home/")
    return render(request, "emp/add_emp.html",{})



def sign_up(request):
    if request.method=='POST':
        name=request.POST.get('naam')
        email_id=request.POST.get('email')
        password=request.POST.get('pass')
        re_password=request.POST.get('repass')
        role=request.POST.get('role')


        d=Details()
        d.name=name
        d.email_id=email_id
        d.password=password
        d.confirm_password=re_password
        d.role=role

        d.save()

        
    
    
    return render(request, "emp/sign_up.html", {})

