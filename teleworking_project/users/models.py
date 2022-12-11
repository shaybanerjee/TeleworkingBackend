from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

from teleworking_project.hosts.models import Host
from teleworking_project.core.models import BaseModel

class User(BaseModel):
	"""Model representing a user"""
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	date_of_birth = models.DateField()
	email = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.PositiveIntegerField() # TODO - Discuss if there's a way to restrict range of field
	company = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	country = models.CharField(max_length=50, null=True, blank=True)
	profile_picture = models.URLField(null=True, blank=True)
	is_verified = models.BooleanField(default=False)
	phone_number = models.CharField(max_length=12)
	class Meta:
		db_table = '"User"'

class UserReview(BaseModel):
 	"""Model representing a user"""
 	user = models.ForeignKey(User, on_delete=models.CASCADE)
 	host = models.ForeignKey(Host, null=True, blank=True, on_delete=models.SET_NULL)
 	rating = models.PositiveIntegerField() # TODO - Discuss if there's a way to restrict range of field
 	review_comment = models.CharField(max_length=200, null=True, blank=True)
 	recommendation = models.BooleanField(default=False)
 	class Meta:
 		db_table = '"UserReview"'


