# Generated by Django 3.0.3 on 2020-05-13 02:35

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_auto_20200513_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, default='none/no-img.jpeg', null=True, upload_to=''),
        ),
    ]
