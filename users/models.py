from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles:
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )


class User(AbstractUser):
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(
        max_length=36,
        blank=True,
        editable=False,
        null=True,
        unique=True
    )
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER)
    bio = models.TextField(blank=True)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == UserRoles.MODERATOR
