# Generated by Django 3.1.1 on 2020-10-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201014_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Publish Date & Time'),
        ),
    ]
