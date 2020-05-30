from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			"id",
			"username",
			"first_name",
			"last_name",
			"email",
			"is_staff",
			"is_active",
			"is_superuser",
		)