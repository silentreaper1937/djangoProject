from django.db import models

# Create your models here.


class UserInfo(models.Model):

    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    token = models.CharField(verbose_name='TOKEN', max_length=64, blank=True, null=True)


class Depart(models.Model):

    title = models.CharField(verbose_name='部门', max_length=32)


class Member(models.Model):

    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.SmallIntegerField(verbose_name='年龄')
    gender = models.SmallIntegerField(verbose_name='性别', choices=((1, '男'), (2, '女')), default=1)
    depart = models.ForeignKey(verbose_name='部门', to=Depart, on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name='入职时间', auto_now_add=True)
