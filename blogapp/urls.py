from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns=[
    path('',home,name="home"),
    path('home',home,name="home"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('aboutus',aboutus,name="aboutus"),
    path('contactus',contactus,name="contactus"),
    path('feedback',feedback,name="feedback"),
    path('forgetpassword',forgetpassword,name="forgetpassword"),

    path('adddetails',adddetails, name="adddetails"),
    path('user',user,name="user"),
    path('createpost',createpost,name="createpost"),
    path('checkdetails',checkdetails,name="checkdetails"),
    path('search',search,name="search"),
    path('viewpost',viewpost,name="viewpost"),
    path('logout',logout,name='logout'),
    path('addpost',addpost,name="addpost"),
    path('profile',profile,name="profile"),
    path('addcontact',addcontact,name="addcontact"),
    path('favorites',favorites,name="favorites")

]