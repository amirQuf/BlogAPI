from django.urls import path 

from .views import ( Profileview , UserList ,FollowerList
)




app_name = "users"
urlpatterns = [
    path('profile/<int:pk>',Profileview.as_view(), name = 'ProfileAPI'),
    path('user/',UserList.as_view(), name = 'userListAPI'),
    path('follower/<int:pk>',FollowerList.as_view(), name = 'followerAPI'),
   
]
    