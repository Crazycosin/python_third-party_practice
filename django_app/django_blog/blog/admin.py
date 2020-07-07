# - * - coding: utf-8 - * -
from django.contrib import admin
from .models import Article, Person
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "update_time")


class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
# python manage.py createsuperuser
# url /admin
# 查看后台管理 
