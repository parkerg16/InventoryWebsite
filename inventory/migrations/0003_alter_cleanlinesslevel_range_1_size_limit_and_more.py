# Generated by Django 4.2.7 on 2023-11-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_contaminants_contaminant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanlinesslevel',
            name='range_1_size_limit',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cleanlinesslevel',
            name='range_2_size_limit',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cleanlinesslevel',
            name='range_3_size_limit',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cleanlinesslevel',
            name='range_4_size_limit',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cleanlinesslevel',
            name='range_5_size_limit',
            field=models.CharField(max_length=15),
        ),
    ]
