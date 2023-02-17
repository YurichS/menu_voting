from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterEmployeeView, RegisterRestaurantView, LoginView, LogoutView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_employee/', RegisterEmployeeView.as_view()),
    path('register_restaurant/', RegisterRestaurantView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
