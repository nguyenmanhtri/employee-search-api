from django.db import models


class Employees(models.Model):
    class EmployeeStatus(models.TextChoices):
        ACTIVE = "Active"
        NOT_STARTED = "Not started"
        TERMINATED = "Terminated"

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False, unique=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=255, null=False, choices=EmployeeStatus.choices
    )
    company = models.CharField(max_length=255, blank=True, null=True)
