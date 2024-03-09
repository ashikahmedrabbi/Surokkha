from django.db import models
from reglogin.models import  User

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    
    
    def __str__(self):
        return self.user.username
    
    

