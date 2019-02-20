# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from enum import IntEnum
from django.db import models


class EmployeeType(IntEnum):
    GM = 1
    PM = 2
    SM = 3
    FTE = 4


class Employee(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=130, blank=False)
    start_date = models.DateField()
    hours_per_week = models.SmallIntegerField()
    active_profile_type = models.SmallIntegerField(
        default=4,
        choices=[(_.value, _.name) for _ in EmployeeType])
    company_name = models.CharField(max_length=130, blank=True, null=True)
    active = models.BooleanField(default=True)
