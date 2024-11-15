# api/serializers.py
from rest_framework import serializers
from .models import Access, Users, Record

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

        
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['name', 'address', 'age', 'weight', 'mobileNo', 'email', 'height']
        extra_kwargs = {
            'name': {'required': True},
            'address': {'required': True},
            'age': {'required': True},
            'weight': {'required': True},
            'mobileNo': {'required': True},
            'height': {'required': True},
        }
        fields = '__all__'
