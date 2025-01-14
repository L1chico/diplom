# Generated by Django 4.2.6 on 2024-05-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_user_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_image',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user_image',
            name='username',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_image',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
