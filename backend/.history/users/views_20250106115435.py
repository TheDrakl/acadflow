from django.shortcuts import render
from .models import User
from rest_framework import generics
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    CustomTokenObtainPairSerializer,
)
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data["refresh"]

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=60 * 60 * 24 * 7,
        )

        return response


class TokenRefreshView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        print(refresh_token)

        if not refresh_token:
            raise AuthenticationFailed("Refresh token missing or invalid")

        try:
            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)
            return Response({"access": new_access_token}, status=200)
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired refresh token")


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        response = Response(
            {
                "user": {"email": user.email, "name": user.get_full_name()},
                "tokens": {"access": str(access)},
            }
        )

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=False,  # Use True in production
            samesite="None",
            max_age=60 * 60 * 24 * 7,
            path="/",
        )
        return response
max_age=60 * 60 * 24 * 7,

class LogoutView(APIView):
    def post(self, request):
        if "refresh_token" not in request.COOKIES:
            raise AuthenticationFailed("You are not logged in or session is invalid.")
        response = Response({"message": "Logged out successfully"})
        response.delete_cookie(
            key="refresh_token",
            path="/",  # Ensure this is the same as when setting the cookie
            samesite="Strict",  # Ensure this matches the initial cookie
        )

        return response


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token_serializer = CustomTokenObtainPairSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        tokens = token_serializer.validated_data

        return Response(
            {
                "user": serializer.data,
                "tokens": tokens,
            }
        )


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
