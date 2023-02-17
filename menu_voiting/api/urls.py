from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='roles'),
    path('register_user', RegisterUserAPIView.as_view(), name='user-registration'),
    # path('register_restaurant', .as_view(), name='restaurant-registration'),
    # path('register_employee', .as_view(), name='employee-registration'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]