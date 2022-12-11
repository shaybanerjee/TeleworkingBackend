# Django imports
from django.conf import settings
from django.core.files import File

# Serializer imports
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from teleworking_project.hosts.serializers import HostSerializer

# Import users model
from teleworking_project.users.models import (
	User,
	UserReview
)



class TPUserSerializer(serializers.ModelSerializer):
	"""Serializer for User object"""
	class Meta:
		model = User
		fields = [
			"id",
			"date_of_birth",
			"email",
			"first_name",
			"last_name",
			"gender",
			"company",
			"city",
			"country",
			"profile_picture",
			"is_verified",
			"phone_number"]


class UserReviewSerializer(serializers.ModelSerializer):
	"""Serializer for UserReview object"""
	class Meta:
		model = UserReview
		fields = ["id", "user", "host", "rating", "review_comment", "recommendation"]

	def create(self, validated_data):
		# Override default `.create()` method
		user = validated_data.pop('user')
		host = validated_data.pop('host')
		user_review = UserReview.objects.create(host=host, user=user, **validated_data)
		return user_review


