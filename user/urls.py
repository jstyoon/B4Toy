from django.urls import path
from user import views
# 유저 뷰를 불러옵니다
urlpatterns = [
    # 해당 경로의 뷰에 연결됩니다
    # DTL을 사용한다면 namespace를 활용할 수 있지만 
    # 백엔드만 구현하고 Postman을 사용해 테스트할 예정이므로 패스
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
]
