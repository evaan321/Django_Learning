# Generated by Django 4.2.7 on 2023-12-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=20)),
                ('taskDetail', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('assign', models.DateTimeField()),
            ],
        ),
    ]