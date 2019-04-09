# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ID = 'id'
    USERNAME = 'username'
    PASSWORD = 'password'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    CONTACT_NUMBER = 'contact_no'
    GENDER = 'gender'
    EMAIL = 'email'
    IS_ACTIVE = 'is_active'

    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    government_id_type = models.CharField(max_length=15, blank=True, null=True)
    government_id_no = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=256, blank=True, null=True)
    vehicle_name = models.CharField(max_length=212, null=True, blank=True)
    vehicle_number = models.CharField(max_length=212, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    city = models.CharField(max_length=112, null=True, blank=True)
    state = models.CharField(max_length=112, null=True, blank=True)
    country = models.CharField(max_length=112, null=True, blank=True)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['-created_at']


class VehicleNumberImages(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class FineApplied(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fine = models.CharField(max_length=112, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
