# Generated by Django 3.1.1 on 2020-10-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=120)),
                ('img', models.ImageField(upload_to='')),
                ('link', models.URLField()),
            ],
        ),
    ]
