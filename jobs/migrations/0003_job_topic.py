# Generated by Django 2.1.5 on 2021-05-01 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0058_auto_20210501_1519"),
        ("jobs", "0002_auto_20210425_1603"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="topic",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="app.Topic"
            ),
        ),
    ]
