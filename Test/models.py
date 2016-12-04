from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    #user_id = models.IntegerField()
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    role = models.CharField(max_length=256, default='normal')
    log_count = models.IntegerField(default=0)

class UserPost(admin.ModelAdmin):
    #list_display = ('username', 'password')
    list_display = ('id', 'username', 'password', 'role', 'log_count')


admin.site.register(User, UserPost)