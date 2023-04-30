from django.test import TestCase
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your tests here.


class ViewTest(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get 요청")
