# Generated by Django 4.1.7 on 2023-02-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vacancies", "0003_alter_vacancy_options_vacancy_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
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
                ("name", models.CharField(max_length=20, verbose_name="Навыки")),
            ],
            options={
                "verbose_name": "Навык",
                "verbose_name_plural": "Навыки",
            },
        ),
        migrations.AddField(
            model_name="vacancy",
            name="skills",
            field=models.ManyToManyField(to="vacancies.skill"),
        ),
    ]
