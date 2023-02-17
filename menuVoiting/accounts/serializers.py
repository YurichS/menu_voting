from rest_framework import serializers
from .models import User, Employee, Restaurant


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class RegisterEmployeeSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.is_employee = True
        user.save()
        Employee.objects.create(employee=user, first_name=self.validated_data['first_name'],
                                last_name=self.validated_data['last_name'])
        return user


class RegisterRestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["email", "username", "password", "name", "address"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.is_restaurant = True
        user.save()
        Restaurant.objects.create(restaurant=user, name=self.validated_data['name'],
                                  address=self.validated_data['address'])
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        fields = ["email", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }


