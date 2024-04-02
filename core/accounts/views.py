from django.shortcuts import render
from rest_framework import viewsets
from accounts import models,serializers
from rest_framework import status
from rest_framework.response import Response
from django.forms import ValidationError
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomUserSerializer
    queryset = models.User.objects.all()

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES