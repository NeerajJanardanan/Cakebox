from django.contrib.auth.models import User

from api.models import Cake,Cart

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CakeSerializer(serializers.ModelSerializer):
    occasion=serializers.StringRelatedField()
    class Meta:
        model=Cake
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    cake=CakeSerializer(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'
    


