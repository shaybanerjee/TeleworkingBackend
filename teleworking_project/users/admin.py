from django.contrib import admin

from teleworking_project.users.models import (
	User,
	UserReview
)

admin.site.register(User)
admin.site.register(UserReview)
