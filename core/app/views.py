from django.shortcuts import render
from rest_framework.views import APIView
from app import serializers,models
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import viewsets

class TasksViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.tasksSerializer
    queryset = models.tasks.objects.all()