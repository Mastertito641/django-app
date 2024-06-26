# Generated by Django 5.0.2 on 2024-04-05 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0013_person_id_user_alter_cities_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 826857)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 826857)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 827854)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 827854)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 827854)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 827854)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 826857)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 826857)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 825858)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 825858)),
        ),
        migrations.AlterField(
            model_name='student',
            name='cre_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 826857)),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 826857)),
        ),
        migrations.AlterField(
            model_name='user',
            name='cre_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 798419)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 19, 38, 798419)),
        ),
    ]
