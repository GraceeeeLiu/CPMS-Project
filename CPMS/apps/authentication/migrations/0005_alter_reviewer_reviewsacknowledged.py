# Generated by Django 3.2.13 on 2022-07-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_reviewer_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='ReviewsAcknowledged',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No'), (None, 'Undetermined')], default=None, null=True),
        ),
    ]
