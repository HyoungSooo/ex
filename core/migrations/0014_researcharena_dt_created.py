# Generated by Django 4.0.6 on 2022-08-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_purpose_dt_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcharena',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True, default='2020-1-1'),
            preserve_default=False,
        ),
    ]
