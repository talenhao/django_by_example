# -*- coding:utf-8 -*-
from django import forms
from .models import Image
from django.utils.text import slugify
from urllib import request
from django.core.files.base import ContentFile


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            "url": forms.HiddenInput,
        }

    # forms.cleaned_data 对象
    # clean_'field_name'()
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('图片扩展名不正确!')
        return url

    def save(self, commit=True, force_insert=False, force_update=False):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = "{}.{}".format(slugify(image.title),
                                    image_url.rsplit('.', 1)[1].lower())
        response = request.urlopen(image_url)
        # image对象.image_field.save_method()
        # ImageField inherits all attributes and methods from FileField,
        # but also validates that the uploaded object is a valid image.
        # image.FieldFile.save(name, content, save=True)
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
        return image
