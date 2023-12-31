# Generated by Django 4.2.3 on 2023-08-01 20:51

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventory'},
        ),
        migrations.AlterField(
            model_name='inventory',
            name='unit',
            field=models.CharField(max_length=20, validators=[store.validators.validate_unit_of_measure]),
        ),
        migrations.AlterField(
            model_name='inventoryorderitem',
            name='unit',
            field=models.CharField(max_length=20, validators=[store.validators.validate_unit_of_measure]),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_unit',
            field=models.CharField(max_length=50, validators=[store.validators.validate_unit_of_measure]),
        ),
        migrations.AlterField(
            model_name='shoporderitem',
            name='unit',
            field=models.CharField(max_length=20, validators=[store.validators.validate_unit_of_measure]),
        ),
    ]
