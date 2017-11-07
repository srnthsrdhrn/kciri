# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    EMPLOYEE = 0
    SUPERVISOR_PRODUCTION = 1
    SUPERVISOR_PINNER = 2
    SUPERVISOR_QUALITY_CHECKER = 3
    ADMIN = 4
    choices = (
        (EMPLOYEE, "Employee"), (SUPERVISOR_PINNER, " Supervisor Production"), (SUPERVISOR_PINNER, "Supervisor Pinner"),
        (SUPERVISOR_QUALITY_CHECKER, "Supervisor Quality Checker"), (ADMIN, "Admin"))
    account_type = models.IntegerField(choices=choices, default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(User):
    employee_id = models.IntegerField()

    def save(self, *args, **kwargs):
        self.account_type = self.EMPLOYEE
        try:
            id = Employee.objects.all().order_by('-id')[0].id + 1
        except Exception, e:
            id = 1
        self.employee_id = id
        super(Employee, self).save()
