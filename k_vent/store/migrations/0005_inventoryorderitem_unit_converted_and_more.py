# Generated by Django 4.2.3 on 2023-08-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_default_unit_product_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryorderitem',
            name='unit_converted',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shoporderitem',
            name='unit_converted',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
