# Generated by Django 3.0.3 on 2020-05-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_remove_choice_random'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
    ]
