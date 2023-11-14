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
    verifyname,verifypassword='',''
    #verify= LoginDetails.objects.get(username=username)
    details=LoginDetails.objects.all().values()
    #print(details,username)
    for x in details:
        if username == x['username']:
            verifyname = x['username']
            verifypassword = x['password']
    
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
    mydict={}
    details=LoginDetails.objects.all().values()
    #print(details,username)
    mydict={
        'verify':False,
        'error':False
    }
    for x in details:
        if username == x['username']:
            mydict['error']=True
            
    if(mydict['error']==False):
        mydict['verify']=True
    myobj = LoginDetails(username=username, password=password)
    myobj.save()
    
    template=loader.get_template('registration.html')
    return HttpResponse(template.render(mydict,request))