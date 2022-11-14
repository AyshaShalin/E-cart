# Generated by Django 4.0.6 on 2022-10-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_firstname', models.CharField(max_length=20)),
                ('c_secondname', models.CharField(max_length=20)),
                ('c_email', models.CharField(max_length=60)),
                ('c_number', models.BigIntegerField()),
                ('c_address', models.CharField(max_length=100)),
                ('c_password', models.CharField(max_length=8)),
            ],
        ),
    ]
