# Generated by Django 2.1.5 on 2021-08-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_auto_20210731_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
