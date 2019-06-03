# Generated by Django 2.1.2 on 2019-05-21 08:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('name_of_taxpayer', models.CharField(default='', max_length=80)),
                ('tin', models.CharField(max_length=15)),
                ('year', models.PositiveIntegerField(blank=True, default='2019', null=True)),
                ('upload_document', models.FileField(upload_to='documents/')),
                ('time_collected', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('recieving_officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turnover_officer_recieving_files', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Turnover', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
