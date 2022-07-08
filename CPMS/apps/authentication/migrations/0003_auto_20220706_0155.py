# Generated by Django 3.2.13 on 2022-07-06 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_auto_20220704_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='Type',
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='Active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.CreateModel(
            name='UserCAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(blank=True, choices=[('Author', 'Author'), ('Reviewer', 'Reviewer'), ('Admin', 'Admin')], max_length=20, null=True)),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='AuthorID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.usercat'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='ReviewerID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.usercat'),
        ),
    ]