# Generated by Django 4.2.7 on 2023-11-17 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_bubblepointlog_mars_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('item_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_type', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('requires_bubble_point', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.itemtype'),
        ),
    ]
