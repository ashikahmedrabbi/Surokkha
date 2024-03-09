from django.db import models
from datetime import timedelta

from doctor.models import Doctor
from django.db import models

from django.contrib.auth.models import User
from reglogin.models import UserAccount

class vaccines(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='vaccines/images/', blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    price = models.IntegerField( blank=True, null=True)
    available_date=models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    name = models.CharField(max_length=30)
    vaccines = models.ForeignKey(vaccines, on_delete=models.CASCADE,related_name='reviews')
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"reviews by {self.name}"

class borrow(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    Vaccines = models.ForeignKey(vaccines, on_delete=models.CASCADE)
    first_dose_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
            
            if not self.first_dose_date and self.Vaccines:
                self.first_dose_date = self.Vaccines.available_date
            super().save(*args, **kwargs)
    
    
    @property
    def second_dose_date(self):
        if self.first_dose_date:
            return self.first_dose_date + timedelta(days=7)
        return None
    
    def __str__(self):
        return f" borrowed {self.Vaccines.name}"