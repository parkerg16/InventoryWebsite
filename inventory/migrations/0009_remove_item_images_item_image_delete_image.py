# Generated by Django 4.2.7 on 2023-11-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_image_remove_itemtype_manufacturer_manufacturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='images',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
