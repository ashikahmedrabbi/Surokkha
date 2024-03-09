from django.contrib import admin

# Register your models here.
from .models import vaccines
from .models import Review
from .models import borrow
admin.site.register(vaccines)
admin.site.register(Review)
admin.site.register(borrow)
