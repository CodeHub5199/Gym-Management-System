# Generated by Django 4.2.4 on 2023-09-08 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0019_alter_member_name_alter_member_updated_plan_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_plan_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 13, 8, 734412, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 13, 8, 735709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 13, 13, 8, 735709, tzinfo=datetime.timezone.utc)),
        ),
    ]
