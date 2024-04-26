# Generated by Django 5.0.2 on 2024-04-26 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0015_remove_user_cre_at_remove_user_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 698332)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 698332)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 699885)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 699885)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 699329)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 699329)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 697335)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 697335)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 648580)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 648580)),
        ),
        migrations.AlterField(
            model_name='student',
            name='cre_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 697335)),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 25, 33, 697335)),
        ),
    ]