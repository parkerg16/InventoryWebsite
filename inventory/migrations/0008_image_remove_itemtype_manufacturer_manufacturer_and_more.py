# Generated by Django 4.2.7 on 2023-11-17 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_itemtype_alter_item_item_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='itemtype',
            name='manufacturer',
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manufacturer_id', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturer_name', models.CharField(max_length=100)),
                ('manufacturer_description', models.CharField(max_length=255)),
                ('manufacturer_website', models.CharField(max_length=255)),
                ('manufacturer_address', models.CharField(max_length=255)),
                ('manufacturer_image', models.ImageField(upload_to='manufacturer_logos/')),
                ('manufacturer_item_types', models.ManyToManyField(to='inventory.itemtype')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='items', to='inventory.image'),
        ),
        migrations.AddField(
            model_name='item',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.manufacturer'),
        ),
    ]
