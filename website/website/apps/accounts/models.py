from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserPersona(models.Model):
    name = models.CharField(max_length = 64 , unique = True)
    normalized_name = models.CharField(max_length = 64 , unique = True)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")

    is_full_name_displayed = models.BooleanField(default=True)

    bio = models.CharField(max_length=500 , blank = True , null=True)
    website = models.URLField(max_length=250 , blank = True , null = True)
    person = models.ForeignKey(UserPersona , on_delete = models.SET_NULL , blank = True , null = True)