from django.shortcuts import render
from .forms import myform
from .models import Course
from django.http import HttpResponseRedirect
# Create your views here.


def thankyou(request):
    return render(request,"courses/success.html")

def mycourse(request):
    if(request.method=="POST"):
        fm=myform(request.POST)
        if(fm.is_valid()):
            print("Name : ",fm.cleaned_data["Name"])
            print("Email : ",fm.cleaned_data["Email"])
            print("Pass : ",fm.cleaned_data["Password"])
            nm=fm.cleaned_data["Name"]
            em=fm.cleaned_data["Email"]
            pw=fm.cleaned_data["Password"]
            c1=Course(Name=nm,Email=em,Password=pw)
            c1.save()
            return HttpResponseRedirect("succ/")            
    else:
        fm=myform()
    return render(request,'courses/base.html',{"form":fm})
