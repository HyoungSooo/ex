# Generated by Django 4.0.6 on 2022-10-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_tasks_alter_aboutus_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='category',
            field=models.CharField(choices=[('International Papers', 'International Papers'), ('International Conference', 'International Conference'), ('Domestic Papers', 'Domestic Papers'), ('Domestic Conference', 'Domestic Conference'), ('Patents', 'Patents')], max_length=500),
        ),
    ]
