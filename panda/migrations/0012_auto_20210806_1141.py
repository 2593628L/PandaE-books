# Generated by Django 2.1.5 on 2021-08-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0011_auto_20210806_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
