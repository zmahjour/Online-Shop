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


class UserRegisterView(APIView):
    authentication_classes = []

    def post(self, request):
        serialized_data = UserRegisterSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(data=serialized_data.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serialized_data = UserLoginSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            phone_number = serialized_data.validated_data.get("phone_number")
            user = User.objects.filter(phone_number=phone_number).exists()

            if not user:
                return Response(
                    {"message": "Any user does not exist with this phone number."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            random_code = set_otp(phone_number=phone_number)
            cache.set(key=phone_number, value=random_code, timeout=120)
            request.session["phone_number"] = phone_number
            return Response({"message": "Verification code has been sent to you."})


class UserVerificationView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serialized_data = UserVerificationSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            otp_code = serialized_data.validated_data.get("otp_code")
            phone_number = request.session.get("phone_number")

            if not cache.get(phone_number):
                raise ValueError

            if cache.get(phone_number) == otp_code:
                user = User.objects.get(phone_number=phone_number)
                jwt_token = JWTToken()
                jti = jwt_token.jti
                access_token = jwt_token.generate_access_token(user=user)
                refresh_token = jwt_token.generate_refresh_token(user=user)
                refresh_exp_seconds = settings.REFRESH_EXPIRE_TIME.total_seconds()

                cache.set(key=jti, value="whitelist", timeout=refresh_exp_seconds)

                return Response(
                    data={
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }
                )
