# Generated by Django 4.0.5 on 2022-06-17 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0016_alter_setoran_checkbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setoran',
            name='checkbox',
        ),
    ]
