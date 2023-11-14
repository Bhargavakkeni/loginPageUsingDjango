from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginDetails
from django.template import loader
# Create your views here.
def root(request):
    return HttpResponse('Server has started')
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

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
    template = loader.get_template('index.html')
    return HttpResponse(template.render(mydict,request))

def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())

def uploading(request):
    username=request.GET['userName']
    password=request.GET['password']
    vobj=LoginDetails.objects.filter(username=username).values()
    mydict={}
    myobj = LoginDetails(username=username, password=password)
    myobj.save()
    template=loader.get_template('registration.html')
    return HttpResponse(template.render(mydict,request))