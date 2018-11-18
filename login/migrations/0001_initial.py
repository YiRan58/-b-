# Generated by Django 2.1.3 on 2018-11-18 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cs',
            fields=[
                ('csId', models.IntegerField(primary_key=True, serialize=False)),
                ('csAdd', models.CharField(max_length=50)),
                ('csStates', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Cs')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userTel', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=16)),
                ('userMail', models.CharField(max_length=20)),
                ('userPwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='usercs',
            name='userTel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Users'),
        ),
    ]
