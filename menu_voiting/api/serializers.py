from rest_framework import serializers
from .models import *

from django.contrib.auth.models import (
    Group
)


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    category = CategorySerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            "category",
            "groups"

        ]


class UserLoginSerializer(serializers.Serializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    password = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
        read_only_fields = ('id',)


class CreateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'name',
            'address',
        ]
        model = Restaurant


class UploadMenuSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        menu = Menu(
            menu=validated_data['menu'],
            restaurant=validated_data['restaurant'],
        )
        menu.save()
        return menu

    class Meta:
        fields = [
            'restaurant',
            'menu',

        ]
        model = Menu


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    employee_no = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuListSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class ResultMenuListSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'id',
            'menu',
            'restaurant',
            'votes',
        ]
