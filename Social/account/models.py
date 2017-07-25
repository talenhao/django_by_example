from django.db import models

# Create your models here.
from django.conf import settings


# 创建扩展model
# Django allows you to override the default user model by providing a value for the AUTH_USER_MODEL setting
# that references a custom model: Default: 'auth.User'
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return "Profile for user {}".format(self.user.username)
