# Generated by Django 3.0.3 on 2020-05-14 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0014_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]