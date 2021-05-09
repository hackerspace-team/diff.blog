# Generated by Django 2.1.5 on 2021-05-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_auto_20210501_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='app.Post')),
            ],
        ),
        migrations.AlterField(
            model_name='blogsuggestion',
            name='status',
            field=models.IntegerField(choices=[(1, 'No GitHub account'), (0, 'Pending'), (2, 'No feed'), (4, 'Non English blog'), (10, 'Blog added'), (3, 'Should be added by the user')], default=0),
        ),
    ]
