# Generated by Django 5.0.4 on 2024-04-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('G', 'General audiences'), ('PG', 'Parental guidance suggested'), ('PG-13', 'Parents strongly cautioned'), ('R', 'Restricted'), ('NC-17', 'Adults Only')], default='G', max_length=20),
        ),
    ]
