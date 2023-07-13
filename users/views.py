from django.contrib.auth.models import User
from rest_framework import exceptions, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serialzers import(GenerateOTPSerializer, 
                        LoginSerializer, 
                        UserSerializer) 


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class SendOTPEmailView(APIView):
    serializer_class = GenerateOTPSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = GenerateOTPSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)

        except exceptions.ValidationError as e:
            return Response({"type": "error", "message": str(e)})

        return Response(
           {
                "type": "success",
                "message": "email has sent.",
                "result": {
                    "email": serializer.data,
                }
           },
           status = status.HTTP_200_SUCCESS,
        )
        

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_serializer = UserSerializer(serializer.validated_data["user"])
        except exceptions.ValidationError as e:
            return Response({"type": "error", "message": str(e)})

        return Response(
            {
                "type": "success",
                "message": "user loged in",
                "result": {
                    "user": user_serializer.data,
                },
            }, status = status.HTTP_200_SUCCESS,
        )


