# Generated by Django 4.1.7 on 2023-04-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp1', '0003_alter_student_dept_alter_student_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Dept',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
