import collections
import datetime
import re
import time

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets, status, permissions, serializers
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserProfile
from users.serializers import UserLoginSerializer, UserRegisterSerializer

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


User = get_user_model()


def return_exception_response(e):
	re_dict = collections.OrderedDict()
	re_dict['code'] = 40050
	re_dict['message'] = str(e)
	return Response(re_dict, status=status.HTTP_200_OK)



class UserLoginUserViewSet(CreateModelMixin, viewsets.GenericViewSet):
	serializers_class = UserLoginSerializer

	def create(self, request, *args, **kwargs):
		try:
			serializer = self.get_serializer(request.data)
			serializer.is_valid(raise_exception=True)

			username = serializer.validated_data.get("username")
			password = serializer.validated_data.get("password")

			this_user = authenticate(username=username, password=password)


		except Exception as e:
			return_exception_response()


class UserRegisterViewSet(CreateModelMixin, viewsets.GenericViewSet):
	serializers_class = UserRegisterSerializer

	def create(self, request, *args, **kwargs):
		try:
			return
		except Exception as e: 
			return_exception_response()