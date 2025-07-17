from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     phone = serializers.CharField(max_length=10)
#     gender = serializers.ChoiceField(choices=['Male', 'Female', 'Other'])
#     state = serializers.CharField(max_length=50)
#     password = serializers.CharField(write_only=True)
#     confirmPassword = serializers.CharField(write_only=True)
#     agree = serializers.BooleanField()

class StudentSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone', 'gender', 'state', 'password', 'confirm_password', 'agree']
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'phone': {'required': True},
            'gender': {'required': True},
            'state': {'required': True},
            'password': {'write_only': True, 'required': True},
            'agree': {'required': True}
        }
        
    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data
