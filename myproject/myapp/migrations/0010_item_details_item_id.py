# Generated by Django 5.0.2 on 2024-03-08 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_item_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_details',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.item'),
        ),
    ]
