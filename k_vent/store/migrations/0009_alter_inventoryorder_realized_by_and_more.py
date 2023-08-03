# Generated by Django 4.2.3 on 2023-08-02 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_inventoryorder_realized_by_shoporder_realized_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryorder',
            name='realized_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='realized_inventory_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shoporder',
            name='realized_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='realized_shop_orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
