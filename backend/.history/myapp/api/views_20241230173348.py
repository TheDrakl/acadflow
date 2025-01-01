from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Hello, world!"}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        return Response(data, status=status.HTTP_201_CREATED)