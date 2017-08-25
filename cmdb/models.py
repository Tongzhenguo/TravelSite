from django.db import models

# Create your models here.
class UserInfo(models.Model):#继承固定写法
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
