from django.db import models

# Create your models here.
from reglogin.models import UserAccount

class Patient(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    first_dose_date = models.DateField(null=True, blank=True)
    second_dose_date = models.DateField(null=True, blank=True)
