# Generated by Django 3.2.6 on 2021-09-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0002_alter_imagefile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='image'),
        ),
    ]