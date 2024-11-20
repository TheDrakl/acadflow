# Generated by Django 5.1.3 on 2024-11-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_teacher_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='teachers', to='myapp.student'),
        ),
    ]
