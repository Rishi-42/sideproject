# Generated by Django 3.2.9 on 2022-07-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='item_image',
            field=models.ImageField(blank=True, upload_to='images/items/'),
        ),
    ]
