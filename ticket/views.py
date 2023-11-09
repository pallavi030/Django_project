from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ticket

def add_ticket (request):
    if request.method=="POST":
        
        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")



        #validate

        #create model object and set the data
        e=Ticket(request.POST)
        # print(e.is_valid())
        e.name=emp_name
        e.emp_id=emp_id
        e.save()
        #prepare msg
        
        return redirect("/ticket/add-ticket/")
    form= Ticket()
    
    return render(request, "ticket/add_tic.html",{'form':form})
