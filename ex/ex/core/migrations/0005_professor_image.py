# Generated by Django 4.0.6 on 2022-07-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_content_alter_professor_greeting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='image',
            field=models.ImageField(default='images/default.jfif', upload_to='images/'),
        ),
    ]