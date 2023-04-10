# Generated by Django 4.1.7 on 2023-03-28 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_pricefortickets_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movingtickets',
            options={'ordering': ['ticket'], 'verbose_name': 'Движение билета', 'verbose_name_plural': 'Движение билетов'},
        ),
        migrations.RenameField(
            model_name='movingtickets',
            old_name='number_ticket',
            new_name='ticket',
        ),
    ]