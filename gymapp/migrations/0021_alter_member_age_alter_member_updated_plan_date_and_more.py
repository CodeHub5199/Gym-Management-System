# Generated by Django 4.2.4 on 2023-09-08 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0020_alter_member_address_alter_member_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_plan_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 13, 57, 835874, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 13, 57, 835874, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 13, 57, 835874, tzinfo=datetime.timezone.utc)),
        ),
    ]