from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = '__all__'