from rest_framework import serializers
from django.db import transaction
from .models import User, UserContact



class RegisterUserSerializer(serializers.ModelSerializer):
    """
        serializer call used to handle the register user
    """
    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=False, min_length=0, max_length=80)
    phone_number = serializers.CharField(required=True, min_length=5, max_length=20)


    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Phone Number already exist.")
        return phone_number

    

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone_number')



class MarkSpamSerializer(serializers.ModelSerializer):
    """
        serializer class used to mark spam
    """
    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=False, min_length=0, max_length=80)
    phone_number = serializers.CharField(required=True, min_length=5, max_length=20)
    

    class Meta:
        model = UserContact
        fields = ('name', 'email', 'phone_number')




class UserSerializer(serializers.ModelSerializer):
    """
        serializer call used to handle the register user
    """

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone_number')



class UserContactDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContact
        fields = ('id', 'name', 'email', 'phone_number', 'is_spam')



class UserDetailSerializer(serializers.ModelSerializer):
    """
        serializer call used to handle the register user
    """
    user_contact = UserContactDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone_number', 'user_contact')

