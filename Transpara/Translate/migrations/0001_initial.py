# Generated by Django 3.2.4 on 2023-09-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_data', models.TextField()),
                ('dateandtime', models.CharField(max_length=30)),
            ],
        ),
    ]
