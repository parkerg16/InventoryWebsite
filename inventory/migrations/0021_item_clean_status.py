# Generated by Django 4.2.7 on 2024-03-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_alter_item_cleanliness_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='clean_status',
            field=models.BooleanField(default=False),
        ),
    ]
