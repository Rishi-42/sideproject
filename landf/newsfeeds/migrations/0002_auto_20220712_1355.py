# Generated by Django 3.2.9 on 2022-07-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='category',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='item_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='location',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
