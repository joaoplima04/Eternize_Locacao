# Generated by Django 5.0.3 on 2024-05-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0004_produto_estilo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estilo',
            field=models.CharField(choices=[('ELEGANTE', 'Elegante'), ('TROPICAL', 'TROPICAL'), ('FLORIDO', 'Florido')], default='', max_length=100),
        ),
    ]
