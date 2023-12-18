# Generated by Django 4.2.7 on 2023-12-18 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_taskcategory_category'),
        ('task', '0002_taskmodel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.taskcategory'),
            preserve_default=False,
        ),
    ]