from rest_framework import serializers
from app import models

class tasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tasks
        fields = ('id','title','description','completed','created_at','user')