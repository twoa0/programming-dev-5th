import re
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from .validators import MinLengthValidator, lnglat_validator, ZipCodeValidator, phone_number_validator
from .fields import PhoneNumberField

class Post(models.Model):
     author = models.CharField(max_length=20, default=1)
     title = models.CharField(max_length=100,
             validators=[MinLengthValidator(4)],
             verbose_name='제목')
     content = models.TextField(help_text='Markdown 문법을 써주세요.',
             validators=[MinLengthValidator(10)])
     tag_set = models.ManyToManyField('Tag', blank=True)
     lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
     created_at = models.DateTimeField(default=timezone.now)
     test_field = models.IntegerField(default=10)

     def get_absolute_url(self):
        return reverse('blog.views.post_detail', args=[self.pk])


class Comment(models.Model):
     post = models.ForeignKey(Post)
     message = models.TextField()
     author = models.CharField(max_length=20)


class Tag(models.Model):
     name = models.CharField(max_length=20)

     def __str__(self):
         return self.name

class Contact(models.Model):
     name = models.CharField(max_length=20)
     phone_number = PhoneNumberField()

class ZipCode(models.Model):
     city = models.CharField(max_length=20)
     road = models.CharField(max_length=20)
     dong = models.CharField(max_length=20)
     gu = models.CharField(max_length=20)
     code = models.CharField(max_length=7)