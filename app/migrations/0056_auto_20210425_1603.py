# Generated by Django 2.1.5 on 2021-04-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_auto_20210420_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsuggestion',
            name='status',
            field=models.IntegerField(choices=[(4, 'Non English blog'), (3, 'Should be added by the user'), (1, 'No GitHub account'), (10, 'Blog added'), (0, 'Pending'), (2, 'No feed')], default=0),
        ),
    ]
