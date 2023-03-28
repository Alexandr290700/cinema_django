# Generated by Django 4.1.7 on 2023-03-28 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_employees_jobtitle_places_alter_saloon_count_place_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricefortickets',
            options={'ordering': ['seanse'], 'verbose_name': 'Цена билета', 'verbose_name_plural': 'Цена билетов'},
        ),
        migrations.RemoveField(
            model_name='pricefortickets',
            name='seanses',
        ),
        migrations.AddField(
            model_name='pricefortickets',
            name='seanse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.seans', verbose_name='Сеансы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='places',
            name='saloon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.saloon', verbose_name='Зал'),
        ),
        migrations.AlterField(
            model_name='pricefortickets',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.sectorsaloon', verbose_name='Сектор'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='booking',
            field=models.BooleanField(verbose_name='Бронь'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='creashed',
            field=models.BooleanField(verbose_name='creashed'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.places', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='played',
            field=models.BooleanField(verbose_name='Оплачено'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='seanses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.seans', verbose_name='Сеанс'),
        ),
    ]
