# Generated by Django 4.1.3 on 2022-11-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_address_student_email_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phoneNo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]