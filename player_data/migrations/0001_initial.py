# Generated by Django 5.1.6 on 2025-02-20 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_first', models.CharField(max_length=50)),
                ('name_use', models.CharField(max_length=50)),
                ('name_last', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=3)),
                ('birth_date', models.DateField()),
                ('height_feet', models.PositiveSmallIntegerField(null=True)),
                ('height_inches', models.PositiveSmallIntegerField(null=True)),
                ('weight', models.PositiveSmallIntegerField(null=True)),
                ('throws', models.CharField(max_length=1)),
                ('bats', models.CharField(max_length=1)),
                ('primary_position', models.CharField(max_length=1, null=True)),
            ],
            options={
                'ordering': ['name_last', 'name_first'],
                'indexes': [models.Index(fields=['name_last', 'name_first'], name='player_data_name_la_740214_idx'), models.Index(fields=['team'], name='player_data_team_bb6fb8_idx')],
            },
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('league', models.CharField(max_length=2, null=True)),
                ('org_abbreviation', models.CharField(max_length=3)),
                ('games', models.PositiveSmallIntegerField()),
                ('games_started', models.PositiveSmallIntegerField()),
                ('complete_games', models.PositiveSmallIntegerField()),
                ('games_finished', models.PositiveSmallIntegerField()),
                ('innings_pitched', models.FloatField()),
                ('wins', models.PositiveSmallIntegerField()),
                ('losses', models.PositiveSmallIntegerField()),
                ('saves', models.PositiveSmallIntegerField()),
                ('total_batters_faced', models.PositiveSmallIntegerField()),
                ('at_bats', models.PositiveSmallIntegerField()),
                ('hits', models.PositiveSmallIntegerField()),
                ('doubles', models.PositiveSmallIntegerField()),
                ('triples', models.PositiveSmallIntegerField()),
                ('home_runs', models.PositiveSmallIntegerField()),
                ('bases_on_balls', models.PositiveSmallIntegerField()),
                ('strikeouts', models.PositiveSmallIntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitching', to='player_data.player')),
            ],
            options={
                'ordering': ['year'],
                'indexes': [models.Index(fields=['org_abbreviation'], name='player_data_org_abb_ea7c5d_idx'), models.Index(fields=['wins'], name='player_data_wins_5a27d5_idx')],
            },
        ),
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('league', models.CharField(max_length=2, null=True)),
                ('org_abbreviation', models.CharField(max_length=3)),
                ('plate_appearances', models.PositiveSmallIntegerField()),
                ('at_bats', models.PositiveSmallIntegerField()),
                ('games', models.PositiveSmallIntegerField()),
                ('games_started', models.PositiveSmallIntegerField()),
                ('runs', models.PositiveSmallIntegerField()),
                ('hits', models.PositiveSmallIntegerField()),
                ('doubles', models.PositiveSmallIntegerField()),
                ('triples', models.PositiveSmallIntegerField()),
                ('home_runs', models.PositiveSmallIntegerField()),
                ('bases_on_balls', models.PositiveSmallIntegerField()),
                ('strikeouts', models.PositiveSmallIntegerField()),
                ('sacrifices', models.PositiveSmallIntegerField()),
                ('sacrifice_flies', models.PositiveSmallIntegerField()),
                ('stolen_bases', models.PositiveSmallIntegerField()),
                ('caught_stealing', models.PositiveSmallIntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batting', to='player_data.player')),
            ],
            options={
                'ordering': ['player', 'year'],
                'indexes': [models.Index(fields=['org_abbreviation'], name='player_data_org_abb_7d8798_idx'), models.Index(fields=['runs'], name='player_data_runs_eea5e8_idx')],
            },
        ),
    ]
