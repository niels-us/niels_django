# Generated by Django 3.2.6 on 2021-10-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nielsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]