from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    full_name = models.CharField('本名',default="",blank=True,null=True,max_length=50)
    introduction =models.TextField('紹介文',default="",blank=True,null=True,max_length=2000)
    career = models.TextField('農業歴',default="",blank=True,null=True,max_length=100)
    item=models.TextField('栽培品目',default="",blank=True,null=True,max_length=100)
    updated_at = models.DateTimeField(auto_now=True)


