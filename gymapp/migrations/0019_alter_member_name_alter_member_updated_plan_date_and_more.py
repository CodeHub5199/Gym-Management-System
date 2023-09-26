# Generated by Django 4.2.4 on 2023-09-08 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0018_trainer_age_alter_member_updated_plan_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_plan_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 11, 23, 980650, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 11, 23, 980650, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 11, 23, 980650, tzinfo=datetime.timezone.utc)),
        ),
    ]