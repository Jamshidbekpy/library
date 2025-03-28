from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email kiritish majburiy")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser `is_staff=True` ")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser `is_superuser=True`")

        return self.create_user(username, email, password, **extra_fields)


class MyUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to="profile_picture/", null=True, blank=True
    )
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ["username"]
        verbose_name = "MyUser"
        verbose_name_plural = "MyUsers"

    def __str__(self):
        return self.username
