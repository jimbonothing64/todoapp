# Generated by Django 4.2.3 on 2023-08-15 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_task_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project',
            new_name='project_id',
        ),
    ]