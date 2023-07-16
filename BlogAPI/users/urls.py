from django.urls import path 

from .views import (  UserList , SendOTPEmailView,
)




app_name = "users"
urlpatterns = [
    path('user/',UserList.as_view(), name = 'userListAPI'),
  
   
]
    