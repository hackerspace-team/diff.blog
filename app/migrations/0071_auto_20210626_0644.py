# Generated by Django 2.1.5 on 2021-06-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_auto_20210613_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsuggestion',
            name='status',
            field=models.IntegerField(choices=[(3, 'Should be added by the user'), (4, 'Non English blog'), (0, 'Pending'), (1, 'No GitHub account'), (2, 'No feed'), (10, 'Blog added')], default=0),
        ),
    ]