# Generated by Django 3.2.6 on 2023-04-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20230426_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ad_pictures/'),
        ),
    ]