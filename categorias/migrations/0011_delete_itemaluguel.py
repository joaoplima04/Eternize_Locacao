# Generated by Django 5.0.4 on 2024-05-28 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0010_produto_quantidade_estoque'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemAluguel',
        ),
    ]