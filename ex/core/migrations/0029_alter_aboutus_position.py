# Generated by Django 4.1.2 on 2022-11-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_aboutus_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='position',
            field=models.CharField(choices=[('Professor', '1'), ('PH.D', 'PH.D'), ('PH.D Student', 'PH.D Student'), ('Post Graduate', 'Post Graduate'), ('Undergraduate', 'Undergraduate')], max_length=13),
        ),
    ]
