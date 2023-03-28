# Generated by Django 4.1.7 on 2023-03-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_movingtickets_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movingtickets',
            name='moving_tickets',
            field=models.IntegerField(default=1, verbose_name='Движение билетов'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets',
            name='ticket_number',
            field=models.IntegerField(default=1, verbose_name='Номер билета'),
            preserve_default=False,
        ),
    ]
