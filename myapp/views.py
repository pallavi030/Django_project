from django.http import HttpResponse
from django.shortcuts import render
import datetime



def home(request):
    return render(request,"home.html",data)

    if request.method=='POST':
        check=request.POST['check']
        print(check)

    # date=datetime.datetime.now()
    # isActive=True
    # name="LearnCodeWithMe"
    # list_of_programs=[
    #     'WAP to Check prime number',
    #     'WAP to check even or odd',
    #     'WAP to print pascals triangle'
    # ]
    # student={
    #     'student_name':'Rahul',
    #     'student_college':'xyz',
    #     'student_city':'Bhopal'
    # }
    # data={
    #     'date':date,
    #     'isActive':isActive,
    #     'name':name,
    #     'list_of_programs':list_of_programs,
    #     'student':student
    # }
    # # print("test fuction is called from view")
#     # return HttpResponse("<h1>Hello this is index page</h1>")
#   return render(request,"home.html",data)
    
def about(request):
    return render(request,"about.html",{})
#   return HttpResponse("<h1>This is about page</h1>")
    
def services(request):
    return render(request,"services.html",{})
    
#     # return HttpResponse("<h1>Hello this is service page</h1>")
    # return render(request,"services.html",{})
    