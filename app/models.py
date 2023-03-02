from django.db import models, transaction
from django.db.models import OneToOneField
from django.dispatch.dispatcher import receiver
from django_extensions.db.models import TimeStampedModel
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Employee(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeProfile(TimeStampedModel):
    class Teams(models.TextChoices):
        Product = "product", "Product"
        Engineering = "engineering", "Engineering"
        Marketing = "marketing", "Marketing"

    class Genders(models.TextChoices):
        Female = "female", "Female"
        Male = "male", "Male"
        Other = "other", "Other"

    dob = models.DateField(blank=True, null=True)
    team = models.CharField(
        max_length=50, choices=Teams.choices,
        blank=True, null=True
    )
    address = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=30, choices=Genders.choices,
        blank=True, null=True
    )
    employee = OneToOneField(
        Employee, related_name="profile",
        on_delete=models.deletion.PROTECT
    )

    def __str__(self):
        return f"{self.employee}"


@receiver(post_save, dispatch_uid="create_employee_profile", sender=Employee)
def create_employee_profile(instance, created, **kwargs):
    if created:
        with transaction.atomic():
            EmployeeProfile.objects.create(employee=instance)