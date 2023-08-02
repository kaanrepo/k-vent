# Generated by Django 4.2.3 on 2023-08-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_default_unit_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='default_unit',
            new_name='unit',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='default_unit_modified',
            new_name='unit_converted',
        ),
        migrations.AddField(
            model_name='inventory',
            name='unit_converted',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]