# Generated by Django 4.0.5 on 2022-06-25 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0019_setoran_nilai_setoran_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setoran',
            name='nilai',
        ),
        migrations.RemoveField(
            model_name='setoran',
            name='note',
        ),
    ]
