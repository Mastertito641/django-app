# Generated by Django 5.0.2 on 2024-04-26 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0014_alter_cities_created_at_alter_cities_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cre_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 411116)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 411116)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 411116)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 411116)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 411116)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 411116)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 410120)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 410120)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 381678)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 381678)),
        ),
        migrations.AlterField(
            model_name='student',
            name='cre_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 410120)),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 46, 59, 410120)),
        ),
    ]
