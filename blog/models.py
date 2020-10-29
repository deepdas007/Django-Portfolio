from django.db import models


class Blogs(models.Model):
    blog_title = models.CharField('Title', max_length=20)
    pub_date = models.DateField('Publish Date')
    content = models.TextField('Body')
    head_image = models.ImageField(upload_to='images/')
