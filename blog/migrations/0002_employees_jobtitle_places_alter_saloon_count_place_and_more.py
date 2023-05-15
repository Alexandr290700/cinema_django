# Generated by Django 4.1.7 on 2023-03-28 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "password",
                    models.CharField(max_length=100, verbose_name="Пароль"),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="JobTitle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Должность"),
                ),
            ],
            options={
                "verbose_name": "Должность",
                "verbose_name_plural": "Должности",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Places",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("row_number", models.IntegerField(verbose_name="Номер ряда")),
                ("row_place", models.IntegerField(verbose_name="Номер места")),
            ],
            options={
                "verbose_name": "Место",
                "verbose_name_plural": "Места",
                "ordering": ["saloon"],
            },
        ),
        migrations.AlterField(
            model_name="saloon",
            name="count_place",
            field=models.IntegerField(verbose_name="Количество мест"),
        ),
        migrations.AlterField(
            model_name="saloon",
            name="description",
            field=models.CharField(max_length=50, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="saloon",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Название зала"),
        ),
        migrations.AlterField(
            model_name="saloon",
            name="number_of_places",
            field=models.IntegerField(verbose_name="Номер места"),
        ),
        migrations.AlterField(
            model_name="saloon",
            name="number_of_rows",
            field=models.IntegerField(verbose_name="Номер ряда"),
        ),
        migrations.CreateModel(
            name="Tickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateField(verbose_name="Дата")),
                (
                    "played",
                    models.BooleanField(max_length=10, verbose_name="Оплачено"),
                ),
                (
                    "booking",
                    models.BooleanField(max_length=10, verbose_name="Бронь"),
                ),
                (
                    "creashed",
                    models.BooleanField(max_length=10, verbose_name="creashed"),
                ),
                (
                    "places",
                    models.ForeignKey(
                        max_length=20,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.places",
                        verbose_name="Место",
                    ),
                ),
                (
                    "seanses",
                    models.ForeignKey(
                        max_length=20,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.seans",
                        verbose_name="Сеанс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Билет",
                "verbose_name_plural": "Билеты",
                "ordering": ["seanses"],
            },
        ),
        migrations.CreateModel(
            name="SectorSaloon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название"),
                ),
                (
                    "description",
                    models.CharField(max_length=50, verbose_name="Описание"),
                ),
                (
                    "saloon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.saloon",
                        verbose_name="Зал",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сектор",
                "verbose_name_plural": "Сектора",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="PriceForTickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Цена")),
                (
                    "seanses",
                    models.ForeignKey(
                        max_length=20,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.seans",
                        verbose_name="Сеансы",
                    ),
                ),
                (
                    "sector",
                    models.ForeignKey(
                        max_length=20,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.sectorsaloon",
                        verbose_name="Сектор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Цена билета",
                "verbose_name_plural": "Цена билетов",
                "ordering": ["seanses"],
            },
        ),
        migrations.AddField(
            model_name="places",
            name="saloon",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.saloon",
                verbose_name="Зал",
            ),
        ),
        migrations.CreateModel(
            name="MovingTickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_create", models.DateField(verbose_name="Дата")),
                (
                    "operation",
                    models.CharField(max_length=20, verbose_name="Операция"),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.employees",
                        verbose_name="Сотрудник",
                    ),
                ),
                (
                    "number_ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.tickets",
                        verbose_name="Номер билета",
                    ),
                ),
            ],
            options={
                "verbose_name": "Движение билета",
                "verbose_name_plural": "Движение билетов",
                "ordering": ["number_ticket"],
            },
        ),
        migrations.AddField(
            model_name="employees",
            name="title",
            field=models.ForeignKey(
                max_length=40,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.jobtitle",
                verbose_name="Должность",
            ),
        ),
    ]
