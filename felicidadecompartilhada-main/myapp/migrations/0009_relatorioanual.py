# Generated by Django 5.1.3 on 2025-05-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_remove_crianca_necessidade_especial_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelatorioAnual",
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
                ("titulo", models.CharField(max_length=200)),
                ("imagem", models.ImageField(upload_to="relatorios_imagens/")),
                ("arquivo_pdf", models.FileField(upload_to="relatorios_pdfs/")),
                ("ano", models.IntegerField()),
            ],
        ),
    ]
