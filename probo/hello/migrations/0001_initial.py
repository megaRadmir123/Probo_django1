# Generated by Django 3.2.19 on 2023-05-21 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zametka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('td', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podrobnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TimeField()),
                ('td', models.DateTimeField(auto_now_add=True)),
                ('zametka', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.zametka')),
            ],
            options={
                'verbose_name_plural': 'подробности',
            },
        ),
    ]