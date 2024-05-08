from django.db import models
from django.contrib.auth.models import User
from .constants import role_choices,GENDER_TYPE 




class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    userRole = models.CharField(max_length=10, choices=role_choices)
    nid_no = models.IntegerField(unique=True) 
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    
    def __str__(self):
        return str(self.user.username)
    
   


