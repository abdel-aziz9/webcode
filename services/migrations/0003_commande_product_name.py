# Generated by Django 4.0.6 on 2023-01-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='product_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
