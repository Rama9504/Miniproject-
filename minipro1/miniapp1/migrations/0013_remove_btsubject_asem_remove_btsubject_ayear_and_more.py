# Generated by Django 4.1.7 on 2023-04-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp1', '0012_alter_honorsregistration_honors_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='btsubject',
            name='ASem',
        ),
        migrations.RemoveField(
            model_name='btsubject',
            name='AYear',
        ),
        migrations.RemoveField(
            model_name='btsubject',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='btsubject',
            name='OfferedBy',
        ),
        migrations.RemoveField(
            model_name='btsubject',
            name='Type',
        ),
    ]