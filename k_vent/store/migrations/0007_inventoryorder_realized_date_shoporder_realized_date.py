# Generated by Django 4.2.3 on 2023-08-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_inventory_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryorder',
            name='realized_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='shoporder',
            name='realized_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
