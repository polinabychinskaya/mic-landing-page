# Generated by Django 5.0.6 on 2024-06-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256, verbose_name='Email - Эл. почта')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=10000, verbose_name='Main body - Содержание'),
        ),
    ]