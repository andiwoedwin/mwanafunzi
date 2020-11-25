from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Category, Product
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

# from .models import UserProfile
User = get_user_model()
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
        
        None,
        validated_data['password'])
        # profile=Profile.objects.create(user=user,email=user.email,username=user)
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']
    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email already in use')})
    #     return super().validate(attrs)
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)





class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'image',         
            'status',
        )
        model = Product       

   
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id','name', 'profile_picture', 'location']