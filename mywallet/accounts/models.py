from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.core import validators
import re


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Name', max_length=200)
    email = models.EmailField('Email', max_length=150, unique=True)
    username = models.CharField(
        'Username', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              'Username can only contain letters, digits or the following characters: @/./+/-/_',
                                              'invalid')]
    )

    is_active = models.BooleanField('Is active?', blank=True, default=False)
    is_staff = models.BooleanField('Is admin?', blank=True, default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
