from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(models.Model):
    #user_id = models.IntegerField()
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    role = models.CharField(max_length=256, default='normal')
    log_count = models.IntegerField(default=0)
    last_log_ip = models.IPAddressField()

class UserPost(admin.ModelAdmin):
    #list_display = ('username', 'password')
    list_display = ('id', 'username', 'password', 'role', 'log_count')

class MyUser(AbstractUser):
    log_count = models.IntegerField(default=0)
    last_log_ip = models.IPAddressField(default='0.0.0.0')

    def __str__(self):
        return self.username

class MyUserPost(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'log_count', 'last_log_ip')

#class UserProfile(User):


#admin.site.register(User, UserPost)
admin.site.register(MyUser, MyUserPost)