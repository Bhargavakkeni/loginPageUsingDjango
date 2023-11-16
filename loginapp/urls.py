from django.urls import path
from . import views
urlpatterns=[
    path('',views.root,name='root'), #url when user enter the app
    path('loginpage/',views.index,name='loginpage'), #url for login
    path('verifyUser',views.verifyUser,name='verifyUser'), #url for verification
    path('registration',views.registration,name='registration'), #url for registration
    path('uploading',views.uploading,name='uploading'),     #url for uplading data to the model
    path('loginpage/omsadmin',views.omsadmin,name='omsadmin'), #url for displaying a dummy template when login is successful
]