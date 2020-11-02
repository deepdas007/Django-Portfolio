from django.db import models


class Blogs(models.Model):
    blog_title = models.CharField('Title', max_length=200)
    pub_date = models.DateTimeField('Publish Date & Time')
    content = models.TextField('Body')
    head_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.blog_title

    def summary(self):
        return self.content[:100]

    def pub_date_new(self):
        return self.pub_date.strftime('%b %e %Y')
