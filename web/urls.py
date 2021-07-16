from django.urls import path 

from .views import (PostList ,PosDetail ,CatgoryList,savedPostList , 

)




app_name = "web"
urlpatterns = [
    path('post/',PostList.as_view(), name = 'PostListAPI'),
    path('post/<int:pk>',PosDetail.as_view(), name = 'PosDetailAPI'),
    path('cat/',CatgoryList.as_view(), name = 'catListAPI'),
    path('savedpost/',savedPostList.as_view(), name = 'savedPostListAPI'),
    
]
    