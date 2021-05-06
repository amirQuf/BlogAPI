from django.urls import path
from .views import (PostList ,PosDetail ,CatgoryList,savedPostList , Profileview , UserList ,FollowerList
)




app_name ="API"
urlpatterns = [
    path('post/',PostList.as_view(), name = 'PostListAPI'),
    path('post/<int:pk>',PosDetail.as_view(), name = 'PosDetailAPI'),
    path('cat/',CatgoryList.as_view(), name = 'catListAPI'),
    path('savedpost/',savedPostList.as_view(), name = 'savedPostListAPI'),
    path('profile/<int:pk>',Profileview.as_view(), name = 'ProfileAPI'),
    path('user/',UserList.as_view(), name = 'userListAPI'),
    path('follower/<int:pk>',FollowerList.as_view(), name = 'followerAPI'),
   
]
    