# Generated by Django 4.2.7 on 2024-02-26 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.customer'),
        ),
    ]