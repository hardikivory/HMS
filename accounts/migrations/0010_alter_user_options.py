# Generated by Django 4.0.4 on 2022-07-11 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_delete_guest_guest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id']},
        ),
    ]
