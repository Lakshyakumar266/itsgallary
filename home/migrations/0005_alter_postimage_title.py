# Generated by Django 3.2.9 on 2021-12-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211202_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]