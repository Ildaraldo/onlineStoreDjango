# Generated by Django 4.2.5 on 2023-09-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='активно'),
        ),
    ]
