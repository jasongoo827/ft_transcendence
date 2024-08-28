from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # 아이디는 AbstractUser에 포함되어 있으므로 따로 정의할 필요가 없습니다.
    # 비밀번호 또한 AbstractUser에서 관리하므로 추가 설정이 필요 없습니다.

    nickname = models.CharField(max_length=20, unique=True, verbose_name='닉네임')
    wins = models.PositiveIntegerField(default=0, verbose_name='승')
    losses = models.PositiveIntegerField(default=0, verbose_name='패')
    
    # 친구 관계는 ManyToManyField로 설정합니다.
    friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='friend_set', verbose_name='친구')

    def __str__(self):
        return self.username  # 기본적으로 아이디(=username)로 반환

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자들'
        
Group.user_set.related_name = 'customuser_set'
Permission.user_set.related_name = 'customuser_permissions'