# Generated by Django 3.2.13 on 2022-07-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defaults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnableReviewers', models.BooleanField(default=True)),
                ('EnableAuthors', models.BooleanField(default=True)),
            ],
        ),
    ]