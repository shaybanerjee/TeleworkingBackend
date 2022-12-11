from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from teleworking_project.users.models import User, UserReview
from teleworking_project.users.serializers import TPUserSerializer, UserReviewSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def login_user(request):
    """ User trying to log into site """
    user_name = request.data.get('user_name', None)
    password = request.data.get('password', None)

    user = authenticate(username=user_name, password=password)

    if user is not None:
        teleworking_user = User.objects.filter(user=user).first()
        user_serializer = TPUserSerializer(teleworking_user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get_user(request, token):
    """Get the user from the request"""
    user = User.objects.get(id=token)
    user_serializer = TPUserSerializer(user)

    return Response(user_serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def post_user(request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    user_name = email

    auth_user = AuthUser.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)

    user_serializer = TPUserSerializer(data=request.data)

    if user_serializer.is_valid(raise_exception=True):
        user_serializer.save(user = auth_user)

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    return Response(user_serializer.data, status=status.HTTP_400_BAD_REQUEST)


def patch_user(request, token):
    """ Patch a user """
    user = get_object_or_404(User, id=token)

    user_serializer = TPUserSerializer(user, data=request.data, partial=True)

    if user_serializer.is_valid(raise_exception=True):
        user_serializer.save(user=request.user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    return Response(user_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def get_user_reviews(request, token):
    """ Get the user reviews for a host """
    user_reviews = UserReview.objects.filter(user=token)
    user_reviews_serializer = UserReviewSerializer(user_reviews, many=True)

    return Response(user_reviews_serializer.data)

def post_user_review(request):
    """ Create a user reviews for host """
    user_reviews_serializer = UserReviewSerializer(data=request.data)
    if user_reviews_serializer.is_valid(raise_exception=True):
        user_reviews_serializer.save()
        return Response(user_reviews_serializer.data, status=status.HTTP_201_CREATED)

    return Response(user_reviews_serializer.data, status=status.HTTP_400_BAD_REQUEST)

def patch_user_review(request, token):
    """ Patch user review for host """
    user_review = get_object_or_404(UserReview, id=token)

    user_review_serializer = UserReviewSerializer (
        user_review, data=request.data, partial=True
    )
    if user_review_serializer.is_valid():
        user_review_serializer.save()
        return Response(user_review_serializer.data, status=status.HTTP_200_OK)

    return Response(user_review_serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST", "PATCH"])
def user_router(request, token=None):
    if request.method.lower() == "get":
        return get_user(request, token)
    elif request.method.lower() == "post":
        return post_user(request)
    elif request.method.lower() == "patch":
        return patch_user(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")

@api_view(["GET", "POST", "PATCH"])
def user_review_router(request, token=None):
    if request.method.lower() == "get":
        return get_user_reviews(request, token)

    elif request.method.lower() == "patch":
        return patch_user_review(request, token)
    else:
        raise Exception("Unsupported HTTP method provided")
