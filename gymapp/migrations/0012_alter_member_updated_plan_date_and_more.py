# Generated by Django 4.2.4 on 2023-09-05 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0011_alter_member_updated_plan_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='updated_plan_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 17, 14, 24, 332044, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 17, 14, 24, 332044, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 17, 14, 24, 332044, tzinfo=datetime.timezone.utc)),
        ),
    ]
