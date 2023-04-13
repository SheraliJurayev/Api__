# Generated by Django 4.1.7 on 2023-04-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("subtite", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=200)),
                ("isbn", models.CharField(max_length=13)),
                ("price", models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]
