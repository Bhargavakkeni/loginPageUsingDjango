from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginDetails
# Create your views here.

def index(request):
    return render(request,'index.html')

def verifyUser(request):
    mydict={}
    username=request.GET['userName']
    password=request.GET['password']
    verify= LoginDetails.objects.all()[0]
    verifyname = verify.username
    verifypassword = verify.password
    
    if username==verifyname and password==verifypassword:
        mydict={
            'verify':True,
            'error':False,
            'name':username
        }
        
    else:
        mydict['error']=True

    return render(request,'index.html',context=mydict)