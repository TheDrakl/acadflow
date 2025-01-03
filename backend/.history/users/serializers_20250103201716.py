from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Get the default validated data (access and refresh tokens)
        data = super().validate(attrs)
        user = self.user

        # Add custom claims to the access token
        access = AccessToken(data["access"])
        access["name"] = user.name
        access["email"] = user.email

        # Replace the access token in the response with the updated one
        data["access"] = str(access)

        return data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["firstName"] = user.first_name
        # ...
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "name", "password", "confirm_password"]

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise ValidationError({"password": "Passwords must match"})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        if "username" not in validated_data:
            validated_data["username"] = validated_data["email"]

        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["name"],
            username=validated_data["username"],
        )
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "password"]

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise ValidationError(_('Must include "email" and "password".'))

        # Authenticate the user using email (treated as username) and password
        user = authenticate(
            request=self.context.get("request"), username=email, password=password
        )

        if not user:
            raise ValidationError(
                _("Invalid credentials, unable to log in with provided credentials.")
            )

        data["user"] = user
        return data
