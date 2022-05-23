# Generated by Django 3.2.6 on 2021-08-08 10:39

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.continent')),
                ('country', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='continent', chained_model_field='continent', on_delete=django.db.models.deletion.CASCADE, to='location.country')),
            ],
        ),
    ]
