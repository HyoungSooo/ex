# Generated by Django 4.0.6 on 2022-07-31 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_professor_ordering_alter_aboutus_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/img.jpg', upload_to='post_images'),
        ),
    ]
