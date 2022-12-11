from django.contrib import admin

from teleworking_project.office.models import (
	Office,
	PropertyAmeneties,
	OfficeBooking,
	OfficeImage,
	OfficeReview,
	OfficeLocation,
	Pricing
)

admin.site.register(Office)
admin.site.register(PropertyAmeneties)
admin.site.register(OfficeBooking)
admin.site.register(OfficeImage)
admin.site.register(OfficeReview)
admin.site.register(OfficeLocation)
admin.site.register(Pricing)
