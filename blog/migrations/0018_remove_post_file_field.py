# Generated by Django 2.1.3 on 2019-01-22 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_file_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file_field',
        ),
    ]