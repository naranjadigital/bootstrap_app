# Generated by Django 2.1.3 on 2018-11-23 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=5, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('entero', models.IntegerField(default=0)),
                ('choice', models.CharField(choices=[('A', 'Letra A'), ('B', 'Letra B'), ('C', 'Letra C')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Foranea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='crud',
            name='foranea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backoffice.Foranea'),
        ),
    ]
