# Generated by Django 4.2 on 2023-04-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]
