﻿from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    coins = models.PositiveIntegerField(default=0, null=True)
    college_major = models.CharField(max_length=20, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

class Relationship(models.Model):
    following = models.ForeignKey(User, related_name='following_users', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='follower_users', on_delete=models.CASCADE)


class Coins_Operation(models.Model):
    related_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    money = models.IntegerField()
    operated_time = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=20, blank=True)
