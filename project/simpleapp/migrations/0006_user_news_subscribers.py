# Generated by Django 4.1.1 on 2022-12-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0005_news_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='subscribers',
            field=models.ManyToManyField(to='simpleapp.user'),
        ),
    ]
