from django.urls import path
from .views import UserList, RegisterView, CustomTokenObtainPairView, LoginView, ProfileView, TokenRefreshView
from .views import LoginView

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", UserList.as_view(), name="users"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", )
    path("profile/", ProfileView.as_view(), name="profile"),
]
