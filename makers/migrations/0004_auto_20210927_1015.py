# Generated by Django 3.2.6 on 2021-09-27 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0003_alter_imagefile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(blank=True, default='camera.jpg', null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='makeroption',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='makers.option'),
        ),
    ]
