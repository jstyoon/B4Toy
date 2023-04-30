from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import CustomTokenObtainPairSerializer, ReadUserSerializer, UserSerializer

# signup view
class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            user_name = serializer.validated_data.get('name')
            return Response({"message":f"${user_name}님 가입을 축하합니다!"}, status=status.HTTP_201_CREATED)
        else: 
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
# myprofile view / query set활용
class MyProfileView(APIView):
    def get(self, user_id):
        verified_user = get_object_or_404(User, id=user_id)
        serializer = ReadUserSerializer(verified_user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        verified_user = get_object_or_404(User, id=user_id)
        if request.user == verified_user:
            token = RefreshToken(request.data.get('refresh'))
            print(token)
            token.blacklist() # 정상적인 로그아웃 방법은 아니다
            return Response({"message": "정상적으로 로그아웃 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "비정상적인 접근입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, user_id):
        verified_user = get_object_or_404(User, id=user_id)
        if request.user == verified_user:
            serializer = UserSerializer(verified_user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                update_user_info = ReadUserSerializer(verified_user)
                return Response(update_user_info.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, user_id):
        verified_user = get_object_or_404(User, id=user_id)
        if request.user == verified_user:
            verified_user.delete()
            return Response({"message": "회원 탈퇴가 정상적으로 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer