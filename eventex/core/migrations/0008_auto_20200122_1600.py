# Generated by Django 2.2.4 on 2020-01-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]
