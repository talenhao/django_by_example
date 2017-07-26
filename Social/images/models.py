from django.db import models

# Create your models here.

from django.conf import settings
from django.utils.text import slugify


# 创建DB
# auto_now: when saved
# auto_now_add: when created
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created')
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                  related_name='images_liked',
                                  blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created = models.DateField(auto_now_add=True,
                               db_index=True)

    def __str__(self):
        return self.title

# auto process image slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)