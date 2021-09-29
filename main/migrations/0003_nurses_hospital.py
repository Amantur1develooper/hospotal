# Generated by Django 3.2.7 on 2021-09-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hospital_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurses',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.hospital', verbose_name='Больница'),
        ),
    ]
