from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email must be provided"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        try:
            validate_password(password)
            user.set_password(password)
        except ValidationError as e:
            raise e
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self._create_user(email, password, **extra_fields)
