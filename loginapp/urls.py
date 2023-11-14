from django.urls import path
from . import views
urlpatterns=[
    path('',views.root,name='root'),
    path('loginapp/',views.index,name='loginapp'),
    path('verifyUser',views.verifyUser,name='verifyUser'),
    path('registration',views.registration,name='registration'),
    path('uploading',views.uploading,name='uploading')
]