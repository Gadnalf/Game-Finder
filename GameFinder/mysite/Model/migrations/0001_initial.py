# Generated by Django 3.1 on 2020-09-03 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categories', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GameID',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tally',
            fields=[
                ('tally', models.AutoField(primary_key=True, serialize=False)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.gameid')),
            ],
        ),
        migrations.CreateModel(
            name='SteamLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.gameid')),
                ('steam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.user')),
            ],
        ),
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_op', models.BooleanField(default=False)),
                ('num_players', models.IntegerField(default=None)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.categories')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.gameid')),
            ],
        ),
    ]
