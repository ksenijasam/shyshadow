# Generated by Django 4.2.4 on 2023-09-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapy_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
