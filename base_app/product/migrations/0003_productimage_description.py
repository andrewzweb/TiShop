# Generated by Django 3.1.7 on 2021-03-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
