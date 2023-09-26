# Generated by Django 4.2.4 on 2023-09-05 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0016_trainer_age_alter_member_updated_plan_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='age',
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_plan_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 17, 52, 48, 789303, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 17, 52, 48, 789303, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 17, 52, 48, 789303, tzinfo=datetime.timezone.utc)),
        ),
    ]
