# Generated by Django 3.1.1 on 2020-10-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
