# Generated by Django 2.0.5 on 2018-05-12 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180512_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='created',
        ),
    ]