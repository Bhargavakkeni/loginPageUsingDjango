from django.urls import path
from . import views
urlpatterns=[
    path('',views.root,name='root'),
    path('loginpage/',views.index,name='loginpage'),
    path('verifyUser',views.verifyUser,name='verifyUser'),
    path('registration',views.registration,name='registration'),
    path('uploading',views.uploading,name='uploading'),
    path('loginpage/omsadmin',views.omsadmin,name='omsadmin'),
]