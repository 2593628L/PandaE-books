# Generated by Django 2.1.5 on 2021-08-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0006_remove_comments_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='type',
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=128),
        ),
    ]