# Generated by Django 3.2.9 on 2021-12-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('tags', models.CharField(default='all', max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='static/images/home')),
                ('timeStamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
