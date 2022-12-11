from django.urls import path

from teleworking_project.core import views

urlpatterns = [
    path("contact_us", views.contact_us, name="contact_us")
]