# Generated by Django 2.1.5 on 2019-03-11 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_comment_upvotes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='feed_status',
            field=models.IntegerField(null=True),
        ),
    ]