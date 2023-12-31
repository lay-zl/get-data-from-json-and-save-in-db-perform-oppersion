# Generated by Django 3.2.12 on 2023-04-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_yr', models.CharField(max_length=100)),
                ('intensity', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=100)),
                ('impact', models.CharField(max_length=100)),
                ('added', models.CharField(max_length=100)),
                ('published', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.CharField(max_length=100)),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('likelihood', models.CharField(max_length=100)),
            ],
        ),
    ]
