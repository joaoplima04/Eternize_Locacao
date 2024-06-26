# Generated by Django 5.0.4 on 2024-05-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='', max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('PRATO RASO', 'Prato Raso'), ('GUARDANAPO', 'Guardanapo'), ('TALHER', 'Talher'), ('TACAS', 'Tacas'), ('TRILHOS DE MESA', 'Trilhos de Mesa'), ('SOUPLAT', 'Souplat'), ('JOGO AMERICANO', 'Jogo Americano'), ('CHA E CAFE', 'Cha e Cafe'), ('PRATO SOBREMESA', 'Prato Sobremesa'), ('PORTA GUARDANAPO', 'Porta Guardanapo')], default='', max_length=150),
        ),
    ]
