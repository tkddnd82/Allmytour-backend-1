# Generated by Django 3.2.6 on 2021-09-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0006_auto_20210927_1408'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageFile',
            new_name='IdImage',
        ),
        migrations.RenameField(
            model_name='idimage',
            old_name='image',
            new_name='id_image',
        ),
        migrations.RemoveField(
            model_name='maker',
            name='id_image',
        ),
        migrations.RemoveField(
            model_name='maker',
            name='profile_image',
        ),
        migrations.AlterModelTable(
            name='idimage',
            table='id_images',
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='camera.jpg', null=True, upload_to='image')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makers.maker')),
            ],
            options={
                'db_table': 'profile_images',
            },
        ),
        migrations.CreateModel(
            name='LicenseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_image', models.ImageField(blank=True, default='camera.jpg', null=True, upload_to='image')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makers.maker')),
            ],
            options={
                'db_table': 'lisence_images',
            },
        ),
    ]
