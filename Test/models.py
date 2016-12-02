from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    role = models.CharField(max_length=256, default='normal')

class UserPost(admin.ModelAdmin):
    list_display = ('username', 'password', 'role')

admin.site.register(User, UserPost)