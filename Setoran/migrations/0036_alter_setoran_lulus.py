# Generated by Django 4.0.5 on 2022-09-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0035_alter_setoran_lulus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setoran',
            name='lulus',
            field=models.BooleanField(),
        ),
    ]
