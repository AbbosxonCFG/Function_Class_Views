from xml.dom import ValidationErr
from rest_framework.validators import ValidationError

from rest_framework import serializers
from .models import User

from main.models import Post


class PostSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Post
        exclude=('author',)
        # fields='__all__'


class PostSerilaizerPro(serializers.ModelSerializer):
    class Meta:
        model=Post
        # exclude=('author',)
        fields='__all__'
















class SignUpSerailizer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8, write_only =True)

    class Meta:
        model=User
        fields=['email','username','password','phone']


    def validate(self,attrs):
        email_exists=User.objects.filter(email=attrs['email']).exists()

        # user=User.objects.
        username_exists=User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise ValidationError('username has already been used')
        
        elif email_exists:
            raise ValidationError('email has already been used')


        return super().validate(attrs)


    
        
       
    
    def create(self, validated_data):
        password=validated_data.pop('password')

        user=super().create(validated_data)

        user.set_password(password)

        user.save()
        return user
