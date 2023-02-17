from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterEmployeeSerializer, RegisterRestaurantSerializer, RegisterUserSerializer, \
    LoginSerializer
from django.contrib.auth import authenticate
from .token import refresh_token


# Create your views here.

class RegisterEmployeeView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterEmployeeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterUserSerializer(user, context=self.get_serializer_context()).data,
            "message": "create employee successfully"
        })


class RegisterRestaurantView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterRestaurantSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterUserSerializer(user, context=self.get_serializer_context()).data,
            "message": "create restaurant successfully"
        })


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        tokens = refresh_token(user)
        return Response({
            "email": user.email,
            "username": user.username,
            "Restaurant": user.is_restaurant,
            "token": tokens
        })


class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = request.data["refresh_token"]
        token.blacklist()

        return Response({"text": "Logged out"})
