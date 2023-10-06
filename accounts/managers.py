from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, **other_fields):
        if not phone_number:
            raise ValueError("Users must have phone number")
        if not full_name:
            raise ValueError("Users must have full name")

        user = self.model(
            phone_number=phone_number, full_name=full_name, **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password, **other_fields):
        user = self.create_user(
            phone_number=phone_number,
            full_name=full_name,
            password=password,
            **other_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
