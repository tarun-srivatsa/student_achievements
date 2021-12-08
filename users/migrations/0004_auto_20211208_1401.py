# Generated by Django 3.2.9 on 2021-12-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_counselor_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counselor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='counselor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]
