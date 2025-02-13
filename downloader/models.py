from django.db import models

# Create your models here.


class UserInfo(models.Model):
   # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()    

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 例如添加手机号字段
    phone_number = models.CharField(max_length=15, blank=True, null=True)    

class Douyinvideo(models.Model):
    video_title = models.CharField(max_length=200)  # 视频标题，字符类型，最大长度200
    video_url = models.URLField()  # 视频链接，URL类型
    uploader_name = models.CharField(max_length=100)  # 上传者名称，字符类型，最大长度100
    publish_time = models.DateTimeField()  # 发布时间，日期时间类型
    # 可以根据实际需求添加更多字段    