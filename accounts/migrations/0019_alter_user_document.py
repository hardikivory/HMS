# Generated by Django 4.0.4 on 2022-07-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]
