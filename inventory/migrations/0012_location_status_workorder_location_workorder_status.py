# Generated by Django 4.2.7 on 2023-11-17 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_cleanlinesslevel_cleanliness_level_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='workorder',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.location'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.status'),
        ),
    ]
