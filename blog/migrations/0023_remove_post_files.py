# Generated by Django 2.1.5 on 2019-01-28 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190128_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='files',
        ),
    ]
