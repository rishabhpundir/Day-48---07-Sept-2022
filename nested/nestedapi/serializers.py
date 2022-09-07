from rest_framework import serializers
from .models import School, Class, Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password = make_password(validated_data['password']))
            user.set_password(validated_data['password'])
            user.save()
            return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_name', 'age', 'gender', 'standard', 'school']

class ClassSerializer(serializers.ModelSerializer):
    student_class = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Class
        fields = ['class_standard', 'section', 'school_name', 'student_class']


class SchoolSerializer(serializers.ModelSerializer):
    class_school = ClassSerializer(many=True, read_only=True)
    class Meta:
        model = School
        fields = ['school_name', 'address', 'class_school']
