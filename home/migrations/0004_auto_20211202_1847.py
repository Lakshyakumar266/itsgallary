# Generated by Django 3.2.9 on 2021-12-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_postimage_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='catogery',
            field=models.CharField(default='all', max_length=200),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='desc',
            field=models.TextField(),
        ),
    ]