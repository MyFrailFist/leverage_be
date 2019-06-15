import datetime

import re

from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import UserProfile




User = get_user_model()



class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'



class UserLoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField(required=True,min_length=1, max_length=100, label="用户名", help_text="用户名")
	password = serializers.CharField(required=True,min_length=1, max_length=100, label="密码", help_text="密码")
	class Meta: 	
		model = UserProfile
		fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
	username = serializers.CharField(required=True,min_length=1, max_length=100, label="用户名", help_text="用户名")
	password = serializers.CharField(required=True,min_length=1, max_length=100, label="密码", help_text="密码")
	first_name = serializers.CharField(required=True, min_length=1, max_length=20, label="姓", help_text="姓")
	last_name = serializers.CharField(required=True, min_length=1, max_length=20, label="名", help_text="名")

	class Meta:
		model = UserProfile
		fields = "__all__"