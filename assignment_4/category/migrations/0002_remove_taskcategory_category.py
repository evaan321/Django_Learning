# Generated by Django 4.2.7 on 2023-12-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='category',
        ),
    ]