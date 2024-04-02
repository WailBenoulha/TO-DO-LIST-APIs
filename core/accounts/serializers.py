from rest_framework import serializers
from .models import User
from accounts import models

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name','lastname','address','birth_date']
    extra_kwargs = {
        'password':{
            'write_only':True,
            'style':{'input_type':'password'}
        }
    }    

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            address=validated_data['address'],
            birth_date=validated_data['birth_date'],
        )
        return user