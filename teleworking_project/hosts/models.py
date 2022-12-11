from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

from teleworking_project.core.models import BaseModel, BaseExtensionModel

class Host(BaseModel):
	"""Model representing a host."""
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	city = models.CharField(max_length=64, null=True, blank=True)
	description = models.CharField(max_length=300, null=True, blank=True)
	identity_verified = models.BooleanField(default=False)
	company_name = models.CharField(max_length=50)
	class Meta:
		db_table = '"Host"'

class ContactInformation(BaseExtensionModel):
	"""Model for representing contact information for a Host"""
	host = models.OneToOneField(Host, primary_key=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	number = models.CharField(max_length=30, null=True, blank=True)
	website = models.URLField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)

	class Meta:
		db_table = '"ContactInformation"'
		default_related_name = "contact_information"
 