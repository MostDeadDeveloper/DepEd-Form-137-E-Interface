from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import AccountManager

from core.models import BaseModel


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    username = models.CharField(
        max_length=24,
        unique=False,
        blank=True,
    )
    phone = models.CharField(
        max_length=13,
        unique=False,
        blank=True,
    )
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    middle_name = models.CharField(max_length=15, null=True)


    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return '{} {} {} '.format(
            self.last_name,
            self.first_name,
            self.middle_name,
        )

