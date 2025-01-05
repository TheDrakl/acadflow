# from django.shortcuts import render
# from .models import User
# from rest_framework import generics
# from .serializers import (
#     UserSerializer,
#     UserRegistrationSerializer,
#     UserLoginSerializer,
#     CustomTokenObtainPairSerializer,
# )
# from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework.views import APIView



# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         refresh_token = response.data["refresh"]

#         response.set_cookie(
#             key="refresh_token",
#             value=refresh_token,
#             httponly=True,
#             secure=True,
#             samesite='Strict',
#             max_age=60 * 60 * 24 * 7
#         )

#         del response.data["refresh"]
#         return response
    

# class TokenRefreshView(APIView):
#     def post(self, request, *args, **kwargs):
#         refresh_token = request.COOKIES.get("refresh_token") 
#         if not refresh_token:
#             raise AuthenticationFailed("Refresh token missing or invalid")

#         try:
#             token = RefreshToken(refresh_token)
#             new_access_token = str(token.access_token)
#             return Response({"access": new_access_token}, status=200)
#         except Exception as e:
#             raise AuthenticationFailed("Invalid or expired refresh token")
        

# class LoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = serializer.validated_data["user"]
#         refresh = RefreshToken.for_user(user)
#         access = refresh.access_token

#         response = Response({
#             "user": {"email": user.email, "name": user.get_full_name()},
#             "tokens": {"access": str(access)},
#         })

#         response.set_cookie(
#             key="refresh_token",
#             value=str(refresh),
#             httponly=True,
#             secure=True,  # Use True in production
#             samesite="None",
#             max_age=60 * 60 * 24 * 7,
#         )
#         return response


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class RegisterView(generics.CreateAPIView):
#     serializer_class = UserRegistrationSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token_serializer = CustomTokenObtainPairSerializer(data=request.data)
#         token_serializer.is_valid(raise_exception=True)
#         tokens = token_serializer.validated_data

#         return Response(
#             {
#                 "user": serializer.data,
#                 "tokens": tokens,
#             }
#         )


# class ProfileView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user


from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
        
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()        
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                                    value = data["access"],
                                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                                        )
                csrf.get_token(request)
                email_template = render_to_string('login_success.html',{"username":user.username})    
                login = EmailMultiAlternatives(
                    "Successfully Login", 
                    "Successfully Login",
                    settings.EMAIL_HOST_USER, 
                    [user.email],
                )
                login.attach_alternative(email_template, 'text/html')
                login.send()
                response.data = {"Success" : "Login successfully","data":data}
                
                return response
            else:
                return Response({"No active" : "This account is not active!!"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"},status=status.HTTP_404_NOT_FOUND)
