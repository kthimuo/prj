# Generated by Django 3.1.5 on 2021-01-07 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='prd',
            new_name='smartphone',
        ),
    ]
