# Generated by Django 4.1.7 on 2023-04-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp1', '0010_remove_honorssub_unique_honorssub_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honorssub',
            name='branch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='honorssub',
            name='honors_name',
            field=models.CharField(max_length=50),
        ),
    ]