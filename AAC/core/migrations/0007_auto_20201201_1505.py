# Generated by Django 3.1.2 on 2020-12-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201201_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name_plural': 'Grade'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name_plural': 'Subject'},
        ),
    ]
