# Generated by Django 3.0.3 on 2020-05-13 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_auto_20200513_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='none/no-img.jpeg', null=True, upload_to=''),
        ),
    ]