# Django imports
from django.conf import settings
from django.core.files import File

# Serializers imports
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from teleworking_project.hosts.serializers import HostSerializer
from teleworking_project.users.serializers import TPUserSerializer

# Import office model
from teleworking_project.office.models import (
	PropertyAmeneties,
    Pricing,
    OfficeLocation,
    Office,
    OfficeBooking,
    OfficeImage,
    OfficeReview
)

class PropertyAmenetiesSerializer(serializers.ModelSerializer):
	"""Serializer for Property object"""
	class Meta:
		model = PropertyAmeneties
		fields = ["id", "wifi", "outlet", "monitor", "heating", "air_conditioning", "coffee", "windows", "parking", "parking_cost", "elevator",
        "wheel_chir_access", "adjustable_seating", "other"]

class PricingSerializer(serializers.ModelSerializer):
	"""Serializer for Pricing object"""
	class Meta:
		model = Pricing
		fields = ["id", "currency", "office_type", "hourly_rate", "monthly_rate"]

class OfficeLocationSerializer(serializers.ModelSerializer):
	"""Serializer for OfficeLocation object"""
	class Meta:
		model = OfficeLocation
		fields = "__all__"

class OfficeSerializer(serializers.ModelSerializer):
    """Serializer for Office object"""
    class Meta:
            model = Office
            fields = ["id", "host", "property_ameneties", "noise_level", "description", "office_type", "pricing", "office_location"]

    def create(self, validated_data):
        # Override default `.create()` method
        host = validated_data.pop('host')
        property_ameneties = validated_data.pop('property_ameneties')
        pricing = validated_data.pop('pricing')
        office_location = validated_data.pop('office_location')
        office = Office.objects.create(host=host, property_ameneties=property_ameneties, pricing=pricing, office_location=office_location, **validated_data)
        return office

class OfficeBookingSerializer(serializers.ModelSerializer):
    """Serializer for OfficeBooking object"""
    user = TPUserSerializer()
    office = OfficeSerializer()

    class Meta:
            model = OfficeBooking
            fields = ["id", "user", "office", "start_booking", "end_booking"]

class OfficeImageSerializer(serializers.ModelSerializer):
    """Serializer for OfficeImage object"""

    class Meta:
        model = OfficeImage
        fields = ["id", "office", "image_bucket_link"]

    def create(self, validated_data):
        # Override default `.create()` method
        office = validated_data.pop('office')
        image_bucket_link = validated_data.pop('image_bucket_link')
        office_image = OfficeImage.objects.create(office=office, image_bucket_link=image_bucket_link)
        return office_image

class OfficeReviewSerializer(serializers.ModelSerializer):
    """Serializer for OfficeReview object"""
    user = TPUserSerializer()
    office = OfficeSerializer()

    class Meta:
            model = OfficeReview
            fields = ["id", "user", "office", "rating", "review_comment", "recommendation"]
