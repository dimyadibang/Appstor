# Generated by Django 4.0.5 on 2022-06-15 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0011_kitab_remove_mahasantri_user_alter_mahasantri_jk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setoran',
            old_name='setoran',
            new_name='kitab',
        ),
    ]
