from django.urls import path

from sampleapp import views

urlpatterns=[
    path("",views.home,name="home"),
    path("index",views.index,name="index"),
    path("stu", views.student, name="stu"),
    path("ad", views.admin_1, name="ad"),

    path("stulogin",views.student_login,name="stulogin"),
    path("adlogin", views.admin_login, name="adlogin"),
    path("loginview", views.login_view, name="loginview"),

]