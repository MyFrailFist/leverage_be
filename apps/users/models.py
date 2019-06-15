import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
	"""
	用户
	"""
	first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="姓")
	last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="名")
	password = models.CharField(max_length=1000, blank=True, null=True, verbose_name="密码")
	email = models.EmailField(max_length=50, blank=True, null=True, verbose_name="邮箱")
	name = models.CharField(max_length=100, blank=True, null=True, verbose_name="姓名")

	token_auth = models.CharField(max_length=100, blank=True, null=True, verbose_name="token")
	
	is_deleted = models.CharField(max_length=1, choices=(('0', 'exist'), ('1', 'deleted')), default='0', verbose_name='是否删除')

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "用户"
		verbose_name_plural = verbose_name




