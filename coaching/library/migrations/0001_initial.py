# Generated by Django 4.2.1 on 2023-06-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatNo', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]
