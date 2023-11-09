from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def verifyUser(request):
    mydict={}
    username=request.GET['userName']
    password=request.GET['password']
    verifyname='bhargavakkeni'
    verifypassword='Bhargav@123'

    if username==verifyname and password==verifypassword:
        mydict={
            'verify':True,
            'error':False,
            'name':username
        }
        
    else:
        mydict['error']=True

    return render(request,'index.html',context=mydict)