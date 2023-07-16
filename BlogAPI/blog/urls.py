from django.urls import path
from .views import (PostViewSet ,CatgoryViewSet 
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('posts' , PostViewSet , basename = 'Posts')
router.register('cats' , CatgoryViewSet , basename = 'Cats')


urlpatterns = router.urls