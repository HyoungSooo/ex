# Generated by Django 4.0.6 on 2022-09-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_photovedio_remove_post_thumbnail_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='greeting',
        ),
        migrations.AddField(
            model_name='professor',
            name='member_since',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
    ]
