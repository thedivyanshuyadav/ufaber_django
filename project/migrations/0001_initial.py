# Generated by Django 4.0 on 2021-12-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=4048)),
                ('duration_in_days', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='project_avatar')),
            ],
            options={
                'verbose_name_plural': 'Project',
            },
        ),
    ]
