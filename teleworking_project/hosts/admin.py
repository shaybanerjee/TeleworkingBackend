from django.contrib import admin

from teleworking_project.hosts.models import (
	Host,
	ContactInformation
)

admin.site.register(Host)
admin.site.register(ContactInformation) 
