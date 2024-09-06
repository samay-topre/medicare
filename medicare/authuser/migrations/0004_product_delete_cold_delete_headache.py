# Generated by Django 4.2.3 on 2024-08-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0003_headache'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Cough', 'Cough'), ('Cold', 'Cold'), ('Headache', 'Headache'), ('First Aid', 'First Aid'), ('Skin Care', 'Skin Care'), ('Baby Care Products', 'Baby Care Products'), ('Proteins', 'Proteins'), ('Others', 'Others'), ('Backpain', 'Backpain'), ('Sore Throat', 'Sore Throat'), ('Asthma', 'Asthma'), ('Migraine', 'Migraine'), ('Influenza', 'Influenza'), ('Stomach Ache', 'Stomach Ache'), ('Skin Rashes', 'Skin Rashes')], max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.DeleteModel(
            name='Cold',
        ),
        migrations.DeleteModel(
            name='Headache',
        ),
    ]
