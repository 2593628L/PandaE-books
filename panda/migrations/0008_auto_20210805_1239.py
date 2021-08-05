# Generated by Django 2.1.5 on 2021-08-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0007_auto_20210805_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='book',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='comments',
            field=models.ManyToManyField(to='panda.Comments'),
        ),
    ]