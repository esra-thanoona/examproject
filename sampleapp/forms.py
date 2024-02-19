from django import forms
from django.contrib.auth.forms import UserCreationForm

from sampleapp.models import Student, Login, Admin_1


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields=("username","password1","password2")
class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    date_of_birth=forms.DateField(widget=DateInput)
    class Meta:
        model=Student
        fields='__all__'
        exclude=("user_1",)



class Admin_1Form(forms.ModelForm):
    class Meta:
        model=Admin_1
        fields='__all__'
        exclude=("user_2",)