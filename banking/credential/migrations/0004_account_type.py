# Generated by Django 5.0.1 on 2024-01-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0003_country_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
            ],
        ),
    ]
