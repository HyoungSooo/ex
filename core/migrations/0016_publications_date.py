# Generated by Django 4.0.6 on 2022-08-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_publications'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='date',
            field=models.DateTimeField(default='2020-1-1'),
            preserve_default=False,
        ),
    ]
