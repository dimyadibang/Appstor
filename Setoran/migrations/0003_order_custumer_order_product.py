# Generated by Django 4.0.4 on 2022-04-19 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Setoran.custumer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Setoran.product'),
        ),
    ]
