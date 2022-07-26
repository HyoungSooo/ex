# Generated by Django 4.0.6 on 2022-08-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_researcharena_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='category',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='headerEx',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='join_date',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='ProfTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Education', 'Education'), ('Interest', 'Interest'), ('Experience', 'Experience')], max_length=12)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MemberReaSearch', to='core.professor')),
            ],
        ),
        migrations.CreateModel(
            name='MembersTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Education', 'Education'), ('Interest', 'Interest'), ('Experience', 'Experience')], max_length=12)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MemberReaSearch', to='core.aboutus')),
            ],
        ),
    ]
