# Generated by Django 5.1.3 on 2024-11-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_alter_crianca_filial_alter_filial_nome_filial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="responsavel",
            name="grau_de_parentesco",
            field=models.CharField(default="null", max_length=50),
            preserve_default=False,
        ),
    ]
