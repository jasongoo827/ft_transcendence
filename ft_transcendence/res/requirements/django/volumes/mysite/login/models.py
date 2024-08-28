from django.db import models

# Create your models here.
class User(models.Model):
	oauthid = models.CharField(max_length=255, unique=True)
	nickname = models.CharField(max_length=20, unique=True, verbose_name='닉네임')
	wins = models.PositiveIntegerField(default=0, verbose_name='승')
	losses = models.PositiveIntegerField(default=0, verbose_name='패')
	friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='friend_set', verbose_name='친구')
	
	def __str__(self):
		return self.oauthid  # 기본적으로 아이디(=oauthid)로 반환
	
	class Meta:
		verbose_name = '사용자'
		verbose_name_plural = '사용자들'