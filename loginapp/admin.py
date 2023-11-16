from django.contrib import admin
from .models import LoginDetails
# Register your models here.

class ListLoginDetails(admin.ModelAdmin):
    list_display=('username','password') #displays the table in a list rather than as a objects

admin.site.register(LoginDetails,ListLoginDetails) #registers model i.e database table in the admin page to view from the browser