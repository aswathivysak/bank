# Generated by Django 5.0.1 on 2024-01-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmname', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pics')),
                ('about', models.TextField()),
            ],
        ),
    ]
