# Generated by Django 3.0.3 on 2020-05-15 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0015_auto_20200514_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respuestas', to='boards.Comentario'),
        ),
    ]