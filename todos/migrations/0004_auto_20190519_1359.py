# Generated by Django 2.2.1 on 2019-05-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20190519_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
