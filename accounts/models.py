
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

ID_LENGTH = 4

    
class User(AbstractUser):
    
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
    
    
    #Guest
    father_name = models.CharField(max_length=100,blank=True)
    room_no = models.IntegerField(null=True, blank=True)
    fees = models.IntegerField(null=True,blank=True)
    work_address = models.CharField(max_length=100,blank=True)
    TYPE = [
        ('NORMAL', 'Normal'),
        ('PREMIUM', 'Premium'),
    ]
    room_type = models.CharField(max_length=100, choices= TYPE, default='NORMAL')
    
    
    #Worker
    salary = models.IntegerField(null=True,blank=True)
    ROLE = [
        ('GARDENER','Gardener'),
        ('CLEANER','Cleaner'),
        ('COOK','Cook'),
        ('SECURITY','Security'),
    ]
    role = models.CharField(max_length=100, choices=ROLE,blank=True)
    current_address = models.CharField(max_length=100,blank=True)
    
    
     

class GuestManager(models.Manager):     
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type= User.Types.GUEST)
    
class Guest(User):   
    objects = GuestManager() 
    
    class Meta:
        proxy = True
 
class WorkerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type= User.Types.WORKER)
    
class Worker(User):   
    objects = WorkerManager()
    class Meta:
        proxy = True
    
 
   
  
  
  
  
   
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
    
    
    
    
    
