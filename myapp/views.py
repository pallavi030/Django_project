from django.shortcuts import render 

def about (request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html",{})

