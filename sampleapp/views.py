from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from sampleapp.forms import LoginRegister, StudentForm, Admin_1Form
from sampleapp.models import Student


# Create your views here.
def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def student(request):
    return render(request,"index.html")

def admin_1(request):
    return render(request, "index.html")


def student_login(request):
    login_form=LoginRegister()
    student_form=StudentForm()
    if request.method=="POST":
        login_form=LoginRegister(request.POST)
        student_form=StudentForm(request.POST,request.FILES)

        if login_form.is_valid() and student_form.is_valid():
            user2=login_form.save(commit=False)
            user2.is_student=True
            user2.save()
            user1=student_form.save(commit=False)
            user1.user_1=user2
            user1.save()
            return redirect("loginview")
    return render(request,"student.html",{'login_form':login_form,'student_form':student_form})


def admin_login(request):
    loginform=LoginRegister
    admin_form=Admin_1Form()
    if request.method=="POST":
        loginform=LoginRegister(request.POST)
        admin_form=Admin_1Form(request.POST)

        if loginform.is_valid() and admin_form.is_valid():
            user2=loginform.save(commit=False)
            user2.is_admin_1=True
            user2.save()
            user1=admin_form.save(commit=False)
            user1.user_2=user2
            user1.save()
            return redirect("loginview")
    return render(request,"admin_1.html",{"loginform":loginform,"admin_form":admin_form})


def login_view(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_student:
                return redirect("stu")
            if user.is_admin_1:
                return redirect("ad")
            else:
                messages.info(request, 'Invalid credentials')
    return render(request, 'login.html')
