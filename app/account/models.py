from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .managers import AccountManager

from core.models import BaseModel


class Account(AbstractBaseUser):
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

    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return '{} {} {} '.format(
            self.last_name,
            self.first_name,
            self.middle_name,
        )

