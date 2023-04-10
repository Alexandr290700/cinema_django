# Generated by Django 3.2 on 2023-04-04 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_movingtickets_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seans',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_session', to='blog.movie', verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='seans',
            name='saloon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saloon_session', to='blog.saloon', verbose_name='Зал'),
        ),
    ]
