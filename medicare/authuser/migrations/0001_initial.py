# Generated by Django 4.2.3 on 2024-07-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cold_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
