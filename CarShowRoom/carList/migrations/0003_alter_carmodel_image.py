# Generated by Django 5.0 on 2024-01-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carList', '0002_alter_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='carList/media/uploads/'),
        ),
    ]