# Generated by Django 3.1.1 on 2020-11-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201029_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
