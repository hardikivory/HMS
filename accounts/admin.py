from django.contrib import admin
from . models import User,Guest,Worker
# Register your models here.




@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'email']
    
    
@admin.register(Guest)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'email']


@admin.register(Worker)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','username','role','email', 'phn_no', 'salary', 'gender', 'current_address' ]
    

    








