# Generated by Django 3.2.13 on 2022-07-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_review_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='Active',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive'), (None, 'Undetermined')], default=True, null=True),
        ),
    ]