from django.contrib import admin

# Register your models here.

from login import models

admin.site.register(models.Users)
admin.site.register(models.Cs)
admin.site.register(models.UserCs)

