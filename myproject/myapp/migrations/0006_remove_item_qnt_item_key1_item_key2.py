# Generated by Django 5.0.2 on 2024-03-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='qnt',
        ),
        migrations.AddField(
            model_name='item',
            name='key1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='key2',
            field=models.IntegerField(default=0, null=True),
        ),
    ]