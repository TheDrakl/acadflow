# Generated by Django 5.1.3 on 2024-11-20 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_teacher_first_name_remove_teacher_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='description',
        ),
    ]