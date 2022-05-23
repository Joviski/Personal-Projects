# Generated by Django 3.2.4 on 2021-06-07 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Equip_Classify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lab_ID', models.CharField(max_length=50)),
                ('lab_deadline', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('task_done', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(null=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('assigned_lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.laboratory')),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.equip_classify')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.currency')),
            ],
        ),
    ]
