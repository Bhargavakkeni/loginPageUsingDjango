from django.contrib import admin
from .models import LoginDetails
# Register your models here.
class ListLoginDetails(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(LoginDetails,ListLoginDetails)