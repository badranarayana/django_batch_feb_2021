# Generated by Django 2.1 on 2021-02-23 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
