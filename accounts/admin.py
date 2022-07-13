from django.contrib import admin
from . models import User,Guest,Worker,Room,RoomType,Contact
# Register your models here.




@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'email', 'profile_pic']
    
    
@admin.register(Guest)
class AdminGuest(admin.ModelAdmin):
    list_display = ['id','username', 'email', 'room_no', 'fees', 'status']


@admin.register(Worker)
class AdminWorker(admin.ModelAdmin):
    list_display = ['id','username','email', 'phn_no','role', 'salary', 'gender', 'current_address' ]
    
    
@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ['room_no', 'room_type', 'room_guest']        
    
    
@admin.register(RoomType)
class AdminRoomType(admin.ModelAdmin):
    list_display = ['my_room_type']    

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phn_no', 'desc']    









