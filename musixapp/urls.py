from django.urls import path
from.views import *


urlpatterns=[
    path('index/',index),
    path('usersignup/', usersignup),
    path('userlogin/', userlogin),
    path('home/', home),
    path('musicdisplay/<int:id>',musicdisplay),
    path('likes/<int:id>',likes),
    path('likedisplay/',likedisplay),
    path('like/<int:id>',liked),
    path('likedelete/<int:id>',likedelete),
    path('logout/',user_logout)


]