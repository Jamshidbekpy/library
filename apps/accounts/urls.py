from rest_framework.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

from .views import (
    UserProfileAPIView,
    RegisterAPIVIew,
    LogoutAPIView,
    ChangePasswordAPIView,
    UpdateProfileAPIView,
)

urlpatterns += [
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("register/", RegisterAPIVIew.as_view(), name="register"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path("update-profile/", UpdateProfileAPIView.as_view(), name="update-profile"),
]
