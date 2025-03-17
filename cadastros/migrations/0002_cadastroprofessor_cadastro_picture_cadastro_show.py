# Generated by Django 5.1.7 on 2025-03-17 17:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroProfessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True)),
                ('show', models.BooleanField(default=True)),
                ('picture', models.ImageField(blank=True, upload_to='pictures/%Y/%m/')),
            ],
        ),
        migrations.AddField(
            model_name='cadastro',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
