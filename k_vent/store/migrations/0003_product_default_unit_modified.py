# Generated by Django 4.2.3 on 2023-08-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_inventory_options_alter_inventory_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='default_unit_modified',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
