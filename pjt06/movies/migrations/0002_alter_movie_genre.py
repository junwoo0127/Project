# Generated by Django 3.2.11 on 2022-04-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('액션', 'action.'), ('스릴러', 'thriller.'), ('코미디', 'comedy')], max_length=30),
        ),
    ]