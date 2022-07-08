from django.contrib import admin
from blog.models import Usuario 
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario,UserAdmin) 

    


