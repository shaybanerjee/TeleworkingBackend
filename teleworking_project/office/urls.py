from django.urls import path

from teleworking_project.office import views

urlpatterns = [
    path("office", views.office_router, name="office"),
    path("office/<uuid:token>", views.office_router, name="office"),
    path("property_ameneties", views.property_ameneties_router, name="property_ameneties"),
    path("property_ameneties/<uuid:token>", views.property_ameneties_router, name="property_ameneties"),
    path("office_booking", views.office_booking_router, name="office_booking"),
    path("office_booking/<uuid:token>", views.office_booking_router, name="office_booking"),
    path("office_image", views.office_image, name="office_image"),
    path("office_image/<uuid:token>", views.office_image, name="office_image"),
    path("office_review", views.office_review, name="office_review"),
    path("office_review/<uuid:token>", views.office_review, name="office_review"),
    path("office_location", views.office_location, name="office_location"),
    path("office_location/<uuid:token>", views.office_location, name="office_location"),
    path("pricing", views.pricing, name="pricing"),
    path("pricing/<uuid:token>", views.pricing, name="pricing")
]
