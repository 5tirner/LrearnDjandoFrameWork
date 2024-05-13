# Generated by Django 5.0.4 on 2024-05-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('clan', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('games', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
            ],
        ),
    ]