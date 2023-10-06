from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.cache import cache
from django.conf import settings
import jwt
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserVerificationSerializer,
)
from .utils import JWTToken
from .models import User
from core.utils import set_otp

