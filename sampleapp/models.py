from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_admin_1=models.BooleanField(default=False)

class Student(models.Model):
    user_1=models.ForeignKey(Login,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    email=models.EmailField()
    Phone_number=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    image = models.FileField(upload_to='images/')

class Admin_1(models.Model):
    user_2=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)