# Generated by Django 3.2.12 on 2022-04-09 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_is_orphan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='is_orphan',
        ),
    ]