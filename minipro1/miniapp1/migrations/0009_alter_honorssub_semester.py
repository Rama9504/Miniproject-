# Generated by Django 4.1.7 on 2023-04-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp1', '0008_alter_honorssub_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honorssub',
            name='semester',
            field=models.IntegerField(null=True),
        ),
    ]
