from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


_key = "abcdefghigklmn"


class UserProfile(AbstractUser):
    """
    用户
    """
    APIkey = models.CharField(max_length=30, verbose_name="APIKey", default=_key)
    money = models.IntegerField(default=10, verbose_name='余额')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Book(models.Model):
    """
    书籍信息
    """
    title = models.CharField(max_length=30, verbose_name='书名', default='')
    isbn = models.CharField(max_length=30, verbose_name='isbn', default='')
    author = models.CharField(max_length=30, verbose_name='作者', default='')
    publish = models.CharField(max_length=30, verbose_name='出版社', default='')
    rate = models.FloatField(verbose_name='豆瓣评分', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title