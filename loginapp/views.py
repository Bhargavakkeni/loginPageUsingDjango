from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginDetails
from django.template import loader
# Create your views here.

#for notifying starting of server
def root(request):
    return HttpResponse('Server has started')

#for displaying login page
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

#for verifying the user login details
def verifyUser(request):
    mydict={}
    username=request.GET['userName']
    password=request.GET['password']
    #print(type(username))
    username=username.strip()
    #print(username,len(username))
    verifyname,verifypassword='',''
    verify= LoginDetails.objects.filter(username=username,password=password).values() #fetch the data from the table which matches the username
    #details=LoginDetails.objects.all().values()
    #print(details,username)
    for x in verify:
        if username == x['username']:
            verifyname = x['username']
            verifypassword = x['password']
    #if verified notifies the user with successful msg
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

#for registration
def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())

#for uplading data to the model
def uploading(request):
    username=request.GET['userName']
    password=request.GET['password']
    username=username.strip()
    mydict={}
    details=LoginDetails.objects.filter(username=username).values()
    #print(details,username)
    mydict={
        'verify':False,
        'error':False
    }
    #check whether user already exist or not
    for x in details:
        if username == x['username']:
            mydict['error']=True  
    #if user doesn't exist create a record and save it
    if(mydict['error']==False):
        mydict['verify']=True
        myobj = LoginDetails(username=username, password=password)
        myobj.save()
    template=loader.get_template('registration.html')
    return HttpResponse(template.render(mydict,request))

#for displaying a dummy template when login is successful
def omsadmin(request):
    template=loader.get_template('OmsAdmin1.html')
    return HttpResponse(template.render())
