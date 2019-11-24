# Generated by Django 2.2.7 on 2019-11-21 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_category_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]