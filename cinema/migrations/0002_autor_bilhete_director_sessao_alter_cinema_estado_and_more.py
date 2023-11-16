# Generated by Django 4.2.7 on 2023-11-15 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('nacionalidade', models.CharField(max_length=80)),
                ('data_nascimento', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Bilhete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('nacionalidade', models.CharField(max_length=80)),
                ('data_nascimento', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('inicio', models.TimeField()),
                ('fim', models.TimeField()),
                ('publico', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
            ],
        ),
        migrations.AlterField(
            model_name='cinema',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
                ('bilhete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.bilhete')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('genero', models.CharField(max_length=80)),
                ('estrangeiro', models.BooleanField(default=False)),
                ('origem', models.CharField(max_length=80)),
                ('duracao', models.TimeField()),
                ('capa', models.ImageField(upload_to='Capa_Filme')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
                ('atores', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.autor')),
                ('cinema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.cinema')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.director')),
            ],
        ),
        migrations.CreateModel(
            name='Cartaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem_cartaz', models.ImageField(blank=True, null=True, upload_to='Imagem_cartaz')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data_criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data_atualização')),
                ('cinema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.cinema')),
            ],
        ),
        migrations.AddField(
            model_name='bilhete',
            name='cinema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.cinema'),
        ),
        migrations.AddField(
            model_name='bilhete',
            name='filme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.filme'),
        ),
        migrations.AddField(
            model_name='bilhete',
            name='sessao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.sessao'),
        ),
    ]
