# Generated by Django 4.1.2 on 2022-11-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traadwik', '0002_jobs_pricelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='contact_email',
            field=models.EmailField(default='careers@traadwik.com', max_length=254),
        ),
    ]
