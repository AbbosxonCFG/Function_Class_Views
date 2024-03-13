
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):


    def create_user(self,email,password,**extra_fields):
        
        email=self.normalize_email(email)
        
        user=self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save()
        return user

  
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            return ValueError("Superuser has to have is_staff  being True")
       
       
        if extra_fields.get('is_superuser') is not True:
            return ValueError("Superuser has to have is_superuser being True")


        return self.create_user(email=email,password=password,**extra_fields)
    
 

    


    
class User(AbstractUser):
    email=models.EmailField(max_length=80,unique=True)
    username=models.CharField(max_length=45,unique=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    date_of_birth=models.DateTimeField(null=True,blank=True)

    objects=CustomUserManager()
    USERNAME_FIELD='username'
    
    REQUIRED_FIELDS=['email',"phone"]
    

    def __str__(self): 
        return self.username 

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser