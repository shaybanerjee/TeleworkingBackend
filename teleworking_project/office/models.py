import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

from teleworking_project.hosts.models import Host 
from teleworking_project.users.models import User
from teleworking_project.core.models import BaseModel

class Office(BaseModel):
        """ Model representing an office for a host. """
        host = models.ForeignKey(Host, on_delete=models.CASCADE, db_index=True)
        property_ameneties = models.ForeignKey("office.PropertyAmeneties", null=True, blank=True, on_delete=models.SET_NULL)
        noise_level = models.PositiveIntegerField()
        description = models.CharField(max_length=400)
        office_type = models.CharField(max_length=50)
        pricing = models.ForeignKey("office.Pricing", null=True, blank=True, on_delete=models.SET_NULL)
        office_location = models.ForeignKey("office.OfficeLocation", null=True, blank=True, on_delete=models.SET_NULL)

class PropertyAmeneties(BaseModel):
        """ Model for the ameneties of a property. """
        wifi = models.BooleanField(default=False)
        outlet = models.BooleanField(default=False)
        monitor = models.BooleanField(default=False)
        heating = models.BooleanField(default=False)
        air_conditioning = models.BooleanField(default=False)
        coffee = models.BooleanField(default=False)
        windows = models.BooleanField(default=False)
        parking = models.BooleanField(default=False)
        parking_cost = models.PositiveIntegerField() #TODO: make nullable
        elevator = models.BooleanField(default=False)
        wheel_chir_access = models.BooleanField(default=False)
        adjustable_seating = models.BooleanField(default=False)
        other = models.CharField(max_length=100)
        class Meta:
                db_table = '"PropertyAmeneties"'

class OfficeBooking(BaseModel):
        """ Model for office booking. """
        user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, db_index=True)
        office = models.ForeignKey(Office, on_delete=models.CASCADE, db_index=True)
        start_booking = models.DateField()
        end_booking = models.DateField()
        class Meta:
                db_table = '"OfficeBooking"'

class OfficeImage(BaseModel):
        """ Model for office image """
        office = models.ForeignKey(Office, on_delete=models.CASCADE, db_index=True)
        image_bucket_link = models.URLField(null=True, blank=True)
        class Meta:
                db_table = '"OfficeImage"'

class OfficeReview(BaseModel):
        """ Model for the review of an office. """
        user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, db_index=True)
        office = models.ForeignKey(Office, on_delete=models.CASCADE, db_index=True)
        rating = models.PositiveIntegerField() #TODO: check if we can set a range
        review_comment = models.CharField(max_length=200)
        recommendation = models.BooleanField(default=False)
        class Meta:
                db_table = '"OfficeReview"'

class OfficeLocation(BaseModel):
        """ Model for the location of the office. """
        postal_code = models.CharField(max_length=6)
        address = models.CharField(max_length=50)
        city = models.CharField(max_length=50)
        province = models.CharField(max_length=50)
        country = models.CharField(max_length=50)
        class Meta:
                db_table = '"OfficeLocation"'

class Pricing(BaseModel):
        """ Model for pricing of office. """
        currency = models.CharField(max_length=10)
        office_type = models.CharField(max_length=10)
        hourly_rate = models.CharField(max_length=15)
        monthly_rate = models.CharField(max_length=15)
        class Meta:
                db_table = '"Pricing"'
