# Generated by Django 2.1.7 on 2019-03-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrap', '0003_auto_20190319_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='header',
        ),
        migrations.AddField(
            model_name='text',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
