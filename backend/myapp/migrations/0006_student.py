# Generated by Django 5.1.3 on 2024-11-20 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_teacher_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher')),
                ('enrolled_companies', models.ManyToManyField(related_name='students', to='myapp.company')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]