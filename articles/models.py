from django.db import models
from accounts.models import User
from datetime import datetime

# Create your models here.

# 할일을 완료한 경우 is_complete를 True로 수정할 수 있어야합니다.
# 완료하지 않은 경우 False로 다시 수정할 수 있어야합니다.
# 제목(title)을 수정할 수 있어야합니다.
class ArticleTodolist(models.Model):
    verified_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_complete = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(default=None, null=True, blank=True)
    
    def __str__(self):
        return str(self.title)

