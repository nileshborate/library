from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["username","password"]
        read_only_fields = ["id"]
    def create(self,validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data['password'])
        user.save()
        return user

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        read_only_fields = ["id"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id"]

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ["id"]

class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnBook
        fields = "__all__"
        read_only_fields = ["id"]