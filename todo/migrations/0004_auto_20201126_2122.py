# Generated by Django 3.1.3 on 2020-11-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201126_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
