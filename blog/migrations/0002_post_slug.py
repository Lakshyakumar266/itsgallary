# Generated by Django 3.2.9 on 2021-12-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='slug', max_length=120),
            preserve_default=False,
        ),
    ]
