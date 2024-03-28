from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    school_id = models.CharField(max_length=10, blank=True)
    school_class = models.CharField(max_length=10, blank=True)
    telephone_number = models.CharField(max_length=15, blank=True)
    can_post = models.DecimalField(max_digits=1, decimal_places=0, default=1)
    is_teacher = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    is_verified = models.DecimalField(max_digits=1, decimal_places=0, default=0)

    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(Permission, related_name='users')


CustomUser = get_user_model()
