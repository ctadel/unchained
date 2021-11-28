# Generated by Django 3.2.9 on 2021-11-27 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_interface', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip_records',
            name='check_counts',
        ),
        migrations.AddField(
            model_name='ip_records',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ip_records',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ip_records',
            name='last_checked',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='ip_records',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]