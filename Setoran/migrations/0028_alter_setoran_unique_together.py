# Generated by Django 4.0.5 on 2022-09-01 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0027_alter_setoran_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='setoran',
            unique_together={('date_created', 'mahasantri', 'kitab')},
        ),
    ]
