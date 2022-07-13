
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
import uuid




# Create your models here.

ID_LENGTH = 4
PASS_LENGTH = 8

def id_gen():
    return str(uuid.uuid4().int)[:ID_LENGTH]

def pass_gen():
    return str(uuid.uuid4())[:PASS_LENGTH]
    
class User(AbstractUser):
    
    password = models.CharField(default=pass_gen, max_length=PASS_LENGTH)
    id = models.AutoField(default=id_gen, max_length=ID_LENGTH, primary_key=True)
    # id = models.PositiveBigIntegerField(primary_key=True)
    class Types(models.TextChoices):
        GUEST ='GUEST', "guest"
        WORKER = 'WORKER', "Worker"
        
    type = models.CharField(max_length=10, choices=Types.choices, default= Types.GUEST) 
    
    
    #common Fields
    age = models.IntegerField(null=True,blank=True)
    GENDER = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    gender = models.CharField(max_length=100, choices=GENDER,blank=True)
    email = models.EmailField(null=True,blank=True)
    phn_no = models.IntegerField(null=True,blank=True)
    native_address = models.CharField(max_length=100,blank=True)
    profile_pic = models.ImageField(upload_to = 'profile', blank=True, null=True)
    document = models.FileField(upload_to='documents', blank=True, null=True)
    
    #Guest fields
    father_name = models.CharField(max_length=100,blank=True)
    room_no = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True)
    fees = models.IntegerField(null=True,blank=True)
    work_address = models.CharField(max_length=100,blank=True)
    
    class Room_Types(models.TextChoices):
        NORMAL ='NORMAL', "normal"
        PREMIUM = 'PREMIUM', "premium"
        
    # room_type = models.ForeignKey('MyRoomType', on_delete=models.CASCADE, null=True, blank=True)
    
    STATUS = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
    ]
    status = models.CharField(max_length=100, choices=STATUS, default='PENDING')
    
    
    #Worker fields
    salary = models.IntegerField(null=True,blank=True)
    ROLE = [
        ('GARDENER','Gardener'),
        ('CLEANER','Cleaner'),
        ('COOK','Cook'),
        ('SECURITY','Security'),
    ]
    role = models.CharField(max_length=100, choices=ROLE,blank=True)
    current_address = models.CharField(max_length=100,blank=True)
    
    
    def __str__(self):
        return str(self.id)
     
    
    class Meta:
        ordering = ['id']
            


#Guest
class GuestManager(BaseUserManager):     
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type= User.Types.GUEST)   
    
class Guest(User):

    email = User.email
    objects = GuestManager() 
    
    class Meta:
        proxy = True
        managed = False
    
  
#Worker
class WorkerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type= User.Types.WORKER)
    
class Worker(User):   
    objects = WorkerManager()
    class Meta:
        proxy = True
        
        
        
  


# #Room
# class RoomManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).all()
    
# class Room(User):
#     objects = RoomManager()
    
#     class Meta:
#         proxy = True    
    
 
   
class Room(models.Model):
    room_no = models.IntegerField(null=True, blank=True)
    room_guest = models.IntegerField(default=0)
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.room_no)
    
class RoomType(models.Model):
    my_room_type = models.CharField(max_length=100, null=True, blank=True)
    my_room_price = models.IntegerField()

    def __str__(self):
        return self.my_room_type
    
  
  
  
class Contact(models.Model):
    
    name = models.CharField(max_length=100)
    phn_no = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
   
# # ABSTRACT MODEL  ( abstract = True )
 
# class common(models.Model):
#     email = models.EmailField()
    
#     class Meta:
#         abstract = True
    

# class Student(common):
#     stu_name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.stu_name
    
    
# class Teacher(common):
#     teach_name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.teach_name
    
    
    
    
    
