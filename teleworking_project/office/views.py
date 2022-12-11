from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework import status

from teleworking_project.office.models import Office, PropertyAmeneties, OfficeBooking, OfficeImage, OfficeReview, OfficeLocation, Pricing
from teleworking_project.office.serializers import OfficeSerializer, PropertyAmenetiesSerializer, OfficeBookingSerializer, OfficeImageSerializer, OfficeReviewSerializer, OfficeLocationSerializer, PricingSerializer

def get_office(request, token):
    """ Get the office from the request """
    office = Office.objects.get(id=token)
    office_serializer = OfficeSerializer(office)

    return Response(office_serializer.data, status=status.HTTP_200_OK)

def post_office(request):
    """ Post office from request """
    office_serializer = OfficeSerializer(data=request.data)

    if office_serializer.is_valid(raise_exception=True):
        office_serializer.save()
        return Response(office_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(office_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
def patch_office(request, token):
    """ Patch a office """
    office = get_object_or_404(Office, id=token)
    office_serializer = OfficeSerializer(office, data=request.data, partial=True)

    if office_serializer.is_valid(raise_exception=True):
        office_serializer.save()
        return Response(office_serializer.data, status=status.HTTP_200_OK)

    return Response(office_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_property_ameneties(request, token):
    """Get the property ameneties from the request"""
    property_ameneties = PropertyAmeneties.objects.get(id=token)
    property_ameneties_serializer = PropertyAmenetiesSerializer(property_ameneties)

    return Response(property_ameneties_serializer.data, status=status.HTTP_200_OK)
 
def post_property_ameneties(request):
    """ Create a property ameneties """
    property_ameneties_serlializer = PropertyAmenetiesSerializer(data=request.data)

    if property_ameneties_serlializer.is_valid(raise_exception=True):
        property_ameneties_serlializer.save()
        return Response(property_ameneties_serlializer.data, status=status.HTTP_201_CREATED)

    return Response(property_ameneties_serlializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_property_ameneties(request, token):
    """ Patch a property_ameneties """
    property_ameneties = get_object_or_404(PropertyAmeneties, id=token)

    property_ameneties_serializer = PropertyAmenetiesSerializer(property_ameneties, data=request.data, partial=True)

    if property_ameneties_serializer.is_valid(raise_exception=True):
        property_ameneties_serializer.save()
        return Response(property_ameneties_serializer.data, status=status.HTTP_200_OK)
    
    return Response(property_ameneties_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_office_booking(request, token):
    """Get the office booking from the request"""
    # TODO: we only want authed users being able to hit this
    office_booking = OfficeBooking.objects.get(id=token)
    office_booking_serializer = OfficeBookingSerializer(office_booking)

    return Response(office_booking_serializer.data, status=status.HTTP_200_OK)

def post_office_booking(request):
    """ Create a office booking """
    office_booking_serializer = OfficeBookingSerializer(data=request.data)

    if office_booking_serializer.is_valid(raise_exception):
        office_booking_serializer.save()
        return Response(office_booking_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(office_booking_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_office_booking(request, token):
    """ Patch a office booking """
    office_booking = get_object_or_404(OfficeBooking, id=token)

    office_booking_serializer = OfficeBookingSerializer(office_booking, data=request.data, partial=True)

    if office_booking_serializer.is_valid(raise_exception=True):
        office_booking_serializer.save()
        return Response(office_booking_serializer.data, status=status.HTTP_200_OK)
    
    return Response(office_booking_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_office_image(request, token):
    """Get the office image from the request """
    office_image = OfficeImage.objects.get(id=token)
    office_image_serializer = OfficeImageSerializer(office_image)

    return Response(office_image_serializer.data, status=status.HTTP_200_OK)

def post_office_image(request):
    """ Create a office image from the request """
    office_image_serializer = OfficeImageSerializer(data=request.data)

    if office_image_serializer.is_valid(raise_exception=True):
        office_image_serializer.save()
        return Response(office_image_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(office_image_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_office_image(request, token):
    """ Patch a office image """
    office_image = get_object_or_404(OfficeImage, id=token)
    
    office_image_serializer = OfficeImageSerializer(office_image, data=request.data, partial=True)

    if office_image_serializer.is_valid(raise_exception=True):
        office_image_serializer.save()
        return Response(office_image_serializer.data, status=status.HTTP_200_OK)

    return Response(office_image_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_office_review(request, token):
    """Get the office review from the request """
    office_review = OfficeReview.objects.get(id=token)
    office_review_serializer = OfficeReviewSerializer(office_review)

    return Response(office_review_serializer.data, status=status.HTTP_200_OK)

def post_office_review(request):
    """ Create a office review from the request """
    office_review_serializer = OfficeReviewSerializer(data=request.data)

    if office_review_serializer.is_valid(raise_exception=True):
        office_review_serializer.save()
        return Response(office_review_serializer.data, status=status.HTTP_201_CREATED)

    return Response(office_review_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_office_review(request, token):
    """ Patch a host """
    office_review = get_object_or_404(OfficeReviewSerializer, id=token)

    office_review_serializer = OfficeReviewSerializer(office_review, data=request.data, partial=True)

    if office_review_serializer.is_valid(raise_exception=True):
        office_review_serializer.save()
        return Response(office_review_serializer.data, status=status.HTTP_200_OK)
    
    return Response(office_review_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_office_location(request, token):
    """ Get the office location from the request """
    office_location = OfficeLocation.objects.get(id=token)
    office_location_serializer = OfficeLocationSerializer(office_location)

    return Response(office_location_serializer.data, status=status.HTTP_200_OK)

def post_office_location(request):
    """ Create a office location from the request """
    office_serializer = OfficeLocationSerializer(data=request.data)
    
    if office_serializer.is_valid(raise_exception=True):
        office_serializer.save()
        return Response(office_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(office_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_office_location(request, token):
    """ Create a office location from the request """
    office_location = get_object_or_404(OfficeLocation, id=token)

    office_location_serializer = OfficeLocationSerializer(office_location, data=request.data, partial=True)

    if office_location_serializer.is_valid(raise_exception=True):
        office_location_serializer.save()
        return Response(office_location_serializer.data, status=status.HTTP_200_OK)
    
    return Response(office_location_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_pricing(request, token):
    """Get the pricing object from the request """
    pricing = Pricing.objects.get(id=token)
    pricing_serializer = PricingSerializer(pricing)

    return Response(pricing_serializer.data, status=status.HTTP_200_OK)

def post_pricing(request):
    """ Create a pricing object from the request """
    pricing_serializer = PricingSerializer(data=request.data)

    if pricing_serializer.is_valid(raise_exception=True):
        pricing_serializer.save()
        return Response(pricing_serializer.data, status=status.HTTP_201_CREATED)
    
    return Repsonse(pricing_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_pricing(request, token):
    """ Patch a pricing object """
    pricing = get_object_or_404(Pricing, id=token)
    pricing_serializer = PricingSerializer(pricing, data=request.data, partial=True)

    if pricing_serializer.is_valid(raise_exception=True):
        pricing_serializer.save()
        return Response(pricing_serializer.data, status=status.HTTP_200_OK)
    
    return Response(pricing_serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST", "PATCH"])
def office_router(request, token=None):
    if request.method.lower() == "get":
        return get_office(request, token)
    elif request.method.lower() == "post":
        return post_office(request)
    elif request.method.lower() == "patch":
        return patch_office(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def property_ameneties_router(request, token=None):
    if request.method.lower() == "get":
        return get_property_ameneties(request, token)
    elif request.method.lower() == "post":
        return post_property_ameneties(request)
    elif request.method.lower() == "patch":
        return patch_property_ameneties(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def office_booking_router(request, token=None):
    if request.method.lower() == "get":
        return get_office_booking(request)
    elif request.method.lower() == "post":
        return post_office_booking(request)
    elif request.method.lower() == "patch":
        return patch_office_booking(request)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def office_image(request, token=None):
    if request.method.lower() == "get":
        return get_office_image(request, token)
    elif request.method.lower() == "post":
        return post_office_image(request)
    elif request.method.lower() == "patch":
        return patch_office_image(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")


@api_view(["GET", "POST", "PATCH"])
def office_review(request, token=None):
    if request.method.lower() == "get":
        return get_office_review(request, token)
    elif request.method.lower() == "post":
        return post_office_review(request)
    elif request.method.lower() == "patch":
        return patch_office_review(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def office_location(request, token=None):
    if request.method.lower() == "get":
        return get_office_location(request, token)
    elif request.method.lower() == "post":
        return post_office_location(request)
    elif request.method.lower() == "patch":
        return patch_office_location(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def pricing(request, token=None):
    if request.method.lower() == "get":
        return get_pricing(request, token)
    elif request.method.lower() == "post":
        return post_pricing(request)
    elif request.method.lower() == "patch":
        return patch_pricing(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")




