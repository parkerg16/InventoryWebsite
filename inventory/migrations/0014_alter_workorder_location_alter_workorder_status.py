# Generated by Django 4.2.7 on 2023-11-20 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_item_model_number_item_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.location'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.status'),
        ),
    ]
