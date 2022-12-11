from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from teleworking_project.users import views

urlpatterns = [
    path("login_user", views.login_user, name="login_user"),
    path("create_user", views.post_user, name="post_user"),
    path("user", views.user_router, name="user"),
    path("user/<uuid:token>", views.user_router, name="user"),
    path("user/user_review", views.user_review_router, name="user_review"),
    path("user/user_review/<uuid:token>", views.user_review_router, name="user_review")
]