# Generated by Django 4.0.4 on 2022-07-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_room_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
