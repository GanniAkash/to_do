# Generated by Django 4.0.6 on 2022-08-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
