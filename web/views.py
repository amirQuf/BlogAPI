from .serializers import (OutputPostSerializer,InputPostSerializer,CategorySerializer , SavePostSerializer ) 
from .models import Post ,Category ,SavePost 
from rest_framework.viewsets import  ModelViewSet


class CatgoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    

class PostViewSet(ModelViewSet):
    queryset =  Post.objects.filter(status='P')
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return OutputPostSerializer
        else:
            return InputPostSerializer
