# Generated by Django 4.0.5 on 2022-06-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Setoran', '0020_remove_setoran_nilai_remove_setoran_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasantri',
            name='status',
            field=models.CharField(blank=True, choices=[('Siswa', 'Siswa'), ('Mahasiswa', 'Mahasiswa')], max_length=200, null=True),
        ),
    ]
