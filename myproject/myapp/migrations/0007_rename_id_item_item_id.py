# Generated by Django 5.0.2 on 2024-03-08 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_item_qnt_item_key1_item_key2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='id',
            new_name='item_id',
        ),
    ]