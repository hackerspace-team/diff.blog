# Generated by Django 2.1.5 on 2021-07-31 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0075_auto_20210731_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cleaned_link',
            new_name='normalized_link',
        ),
    ]