# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from users.models import Employee, User


class DataEntry(models.Model):
    employee = models.ForeignKey(Employee, related_name='worked_entries')
    created_by = models.ForeignKey(User,related_name='entries')
    quality = models.IntegerField(choices=((0, 0), (1, 1), (2, 2), (3, 3)))
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
