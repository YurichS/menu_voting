from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .utils import get_tokens_for_user
from .serializers import *


# Create your views here.

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer


class RegisterUserAPIView(APIView):
    def post(self, request, format=None):
        req = request.data
        user_group, _ = Group.objects.get_or_create(name=req.get('category'))
        category_group, _ = Category.objects.get_or_create(name=req.get('category'))

        serializer = UserSerializer(data=req)

        if serializer.is_valid():
            try:
                new_user = User.objects.create(
                    username=req.get('email'),
                    email=req.get('email'),
                    first_name=req.get('first_name').capitalize(),
                    last_name=req.get('last_name').capitalize(),
                    is_active=True,
                    is_staff=True

                )

                new_user.roles.add(category_group)
                new_user.groups.add(user_group)

                password = User.objects.make_random_password(length=10)
                new_user.set_password(password)
                new_user.save()
                res = {
                    "msg": f"Successfully registered",
                    "data": req,
                    "success": True}
                return Response(data=res, status=status.HTTP_201_CREATED)
            except Exception as e:
                res = {"msg": str(e), "data": None, "success": False}
                return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

        res = {"msg": str(serializer.errors), "data": None, "success": False}
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        try:
            user = User.objects.get(email=request.data["email"])

            if check_password(request.data["password"], user.password):
                token = get_tokens_for_user(request.user)

                user.save()
                res = {
                    "msg": "Login success",
                    "success": True,
                    "data": {
                        "name": user.first_name,
                        "username": user.username,
                        "id": user.id,
                        "token": token,
                        "category": user.category}}
                return Response(data=res, status=status.HTTP_200_OK)

            else:
                res = {
                    "msg": "Invalid login credentials",
                    "data": None,
                    "success": False}
                return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res = {"msg": str(e), "success": False, "data": None}
            return Response(data=res, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    # permission_classes = (IsAuthenticated,)
    #
    # def get(self, request):
    #     try:
    #         username = jwt_decode_handler(request.auth).get('username')
    #         user = User.objects.get(username=username)
    #         payload = jwt_payload_handler(user)
    #         jwt_encode_handler(payload)
    #         res = {
    #             "msg": "User logged out successfully",
    #             "success": True,
    #             "data": None}
    #         return Response(data=res, status=status.HTTP_205_RESET_CONTENT)
    #     except Exception as e:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged Out'}, status=status.HTTP_200_OK)


