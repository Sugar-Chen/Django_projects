from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''图书类'''
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除


class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to='booktest')


class AreaInfo(models.Model):
    '''省市县地区表'''
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self',null=True,blank=True)
