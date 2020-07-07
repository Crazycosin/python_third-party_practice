# - * - coding: utf-8 - * -
from __future__ import unicode_literals
from django.db import models
from six import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField("标题", max_length=256)
    content = models.TextField("内容")
    pub_date = models.DateTimeField("发表时间", auto_now_add=True, editable=True)
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)

    def __str__(self) -> str:
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    
    my_property.short_description = 'Full name of the person'
    full_name = property(my_property)




