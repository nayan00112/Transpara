# Generated by Django 3.2.4 on 2023-09-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_auto_20230916_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdata',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]