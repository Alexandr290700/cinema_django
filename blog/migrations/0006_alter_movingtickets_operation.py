# Generated by Django 4.1.7 on 2023-03-28 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_movingtickets_moving_tickets_tickets_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movingtickets',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Operation', to='blog.tickets', verbose_name='Операция'),
        ),
    ]
