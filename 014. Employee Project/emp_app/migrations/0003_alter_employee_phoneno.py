# Generated by Django 4.1.3 on 2022-11-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_remove_employee_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phoneNo',
            field=models.CharField(max_length=10),
        ),
    ]
