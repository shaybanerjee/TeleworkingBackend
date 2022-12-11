# django imports
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# rest imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework import status

# project imports
from teleworking_project.hosts.models import Host, ContactInformation
from teleworking_project.hosts.serializers import HostSerializer, ContactInformationSerializer

def get_host(request, token):
    """ Get the host from the request """
    host = Host.objects.filter().select_related("contact_information").get(id=token)
    host_serializer = HostSerializer(host)

    return Response(host_serializer.data, status=status.HTTP_200_OK)

def post_host(request):
    """ Create a host """
    post_serializer = HostSerializer(data=request.data)

    if post_serializer.is_valid(raise_exception=True):
        post_serializer.save(user=request.user)
        return Response(post_serializer.data, status=status.HTTP_201_CREATED)

    return Response(post_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_host(request, token):
    """ Patch a host """
    host = get_object_or_404(Host, id=token)
    
    post_serializer = HostSerializer(host, data=request.data, partial=True)
    
    if post_serializer.is_valid(raise_exception=True):
        post_serializer.save(user=request.user)
        return Response(post_serializer.data, status=status.HTTP_200_OK)

    return Response(post_serializer.data, status=status.HTTP_400_BAD_REQUEST)

# currently this endpoint is unsuable since we don't generate an id
# for this object and it can only be accessed and modified via a post/patch/get
# to host
def get_contact_information(request, token):
    """ Get the contact information for a host """
    contact_information = ContactInformation.objects.filter(id=token)
    contact_serializer = ContactInformationSerializer(contact_information)

    return Response(contact_serializer.data, status=status.HTTP_200_OK)

# currently this endpoint is unsuable since we don't generate an id
# for this object and it can only be accessed and modified via a post/patch/get
# to host
def post_contact_information(request):
    """ Create a contact information for host """
    contact_serializer = ContactInformationSerializer(data=request.data)

    if contact_serializer.is_valid(raise_exception=True):
        contact_serializer.save()
        return Response(contact_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(contact_serializer.data, status=status.HTTP_400_BAD_REQUEST)

# currently this endpoint is unsuable since we don't generate an id
# for this object and it can only be accessed and modified via a post/patch/get
# to host
def patch_contact_information(request, token):
    """ Patch contact information for host """
    contact_information = get_object_or_404(ContactInformation, id=token)

    contact_serializer = ContactInformationSerializer(contact_information, data=request.data, partial=True)
    
    if contact_serializer.is_valid(raise_exception=True):
        contact_serializer.save()
        return Response(contact_serializer.data, status=status.HTTP_200_OK)
    
    return Response(contact_serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST", "PATCH"])
def host_router(request, token=None):
    if request.method.lower() == "get":
        return get_host(request, token)
    elif request.method.lower() == "post":
        return post_host(request)
    elif request.method.lower() == "patch":
        return patch_host(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def contact_information_router(request, token=None):
    if request.method.lower() == "get":
        return get_contact_information(request, token)
    elif request.method.lower() == "post":
        return post_contact_information(request)
    elif request.method.lower() == "patch":
        return patch_contact_information(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")
