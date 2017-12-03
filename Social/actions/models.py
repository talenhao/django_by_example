from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# This ContentType is absolute model, has tree Fields.
#   app_label: auto taken from Meta options, eg: python manage.py startapp appname(this name = app_label)
#   model: The name of the model class , get model_name ContentType.objects.get_for_model(Image)
#   name: auto taken from Meta option "verbose_name" attribute
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# contenttypes framework
# track all models installed in your project and provides a generic interface to interact with your models


# 1 数据库
class Actions(models.Model):
    """
    Step1: With this basic model, we can only store actions such as User X did something.
    
    """
    # 2 字段 外链 用户
    # 默认ForeignKey只能关联一个model,在这里需要使用target一个变量关联多个models(Images, User)
    # ContentType关联对多个models,
    # current user 只有一个,可以使用单一关联.
    user = models.ForeignKey(User,
                             # 3 Django关联名称
                             # related_name是关联对象反向引用描述符
                             related_name='actions',
                             # 4.索引
                             db_index=True
                             )
    # Do verb
    verb = models.CharField(max_length=255)
    
    target_content_type = models.ForeignKey(ContentType,
                                            blank=True,
                                            null=True,
                                            related_name="target_obj"
                                            )
    # 自增主键
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True)
    target = GenericForeignKey('target_content_type', 'target_id')

    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True
                                   )

    class Meta:
        ordering = ('-created',)
