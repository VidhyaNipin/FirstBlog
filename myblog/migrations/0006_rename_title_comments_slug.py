# Generated by Django 4.0.5 on 2022-07-11 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_rename_slug_comments_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='title',
            new_name='slug',
        ),
    ]
