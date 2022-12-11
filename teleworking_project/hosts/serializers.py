# Django imports
from django.conf import settings
from django.core.files import File
from django.shortcuts import get_object_or_404

# Serializers imports
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# Import hosts model
from teleworking_project.hosts.models import (
	Host,
	ContactInformation
)

class ContactInformationSerializer(serializers.ModelSerializer):
	"""Serializer for ContactInformation object"""
	class Meta:
		model = ContactInformation
		fields = [
			"first_name",
			"last_name",
			"email",
			"number",
			"website",
			"facebook",
			"instagram",
			"twitter",
		]

class HostSerializer(serializers.ModelSerializer):
	"""Serializer for Host object"""
	contact_information = ContactInformationSerializer()
	class Meta:
		model = Host
		fields = [
			"city",
			"description",
			"identity_verified",
			"contact_information",
			"company_name"
		]
		
	def create(self, validated_data):
		contact_information_data = validated_data.pop("contact_information")
		host = Host.objects.create(**validated_data)

		contact_information = ContactInformation.objects.create(pk=host.pk, **contact_information_data)

		return host

	def update(self, instance, validated_data):
		city = validated_data.pop("city", None)
		description = validated_data.pop("description", None)
		identity_verified = validated_data.pop("identity_verified", None)
		company_name = validated_data.pop("company", None)

		if city:
			instance.city = city
		if description:
			instance.description = description
		if identity_verified:
			instance.identity_verified = identity_verified
		if company_name:
			instance.company_name = company_name

		instance.save()

		contact_information_data = validated_data.pop("contact_information", None)

		if contact_information_data:
			contact_information = get_object_or_404(ContactInformation, host=instance)

			if contact_information:
				# update
				contact_information_serializer = ContactInformationSerializer(contact_information, data=contact_information_data, partial=True)
				    
				if contact_information_serializer.is_valid(raise_exception=True):
					contact_information_serializer.save()
				else:
					print("TODO: throw a exception that will be propogated to FE")
			else:
				# create
				ContactInformation.objects.create(pk = instance.pk, **contact_information_data)


		return instance





		