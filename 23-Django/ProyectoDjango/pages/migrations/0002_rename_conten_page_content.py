# Generated by Django 5.1.7 on 2025-04-08 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='conten',
            new_name='content',
        ),
    ]
