# Generated by Django 5.0.2 on 2024-03-08 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_id_item_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='key3',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
