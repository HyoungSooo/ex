# Generated by Django 4.1.2 on 2022-11-04 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_aboutus_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='publications',
            name='file',
        ),
        migrations.RemoveField(
            model_name='publications',
            name='link',
        ),
    ]
