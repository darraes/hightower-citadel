# Generated by Django 5.0 on 2023-12-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_m2', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
            ],
        ),
    ]
