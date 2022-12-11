from django.urls import path

from teleworking_project.hosts import views

urlpatterns = [
    path("host", views.host_router, name="host"),
    path("host/<uuid:token>", views.host_router, name="host"),
    path("host/contact_information", views.contact_information_router, name="contact_information"),
    path("host/contact_information/<uuid:token>", views.contact_information_router, name="contact_information")
]
