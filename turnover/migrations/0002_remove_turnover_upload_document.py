# Generated by Django 2.1.2 on 2019-06-03 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnover', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnover',
            name='upload_document',
        ),
    ]
