from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User


# 创建扩展model
# Django allows you to override the default user model by providing a value for the AUTH_USER_MODEL setting
# that references a custom model: Default: 'auth.User'
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return "Profile for user {}".format(self.user.username)


# user follow
class Contact(models.Model):
    user_from = models.ForeignKey(User,
                                  related_name='rel_from_set')
    user_to = models.ForeignKey(User,
                                related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} follows {}".format(self.user_from,
                                      self.user_to)

# We are going to take a slightly different approach,
# by adding this field dynamically to the User model.
# Edit the models.py file of the account application and add the following lines:
User.add_to_class("following",
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
