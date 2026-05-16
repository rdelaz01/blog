from django.contrib import admin
from .models import post, Status

# Register your models here.
admin.site.register([post, Status])