# Generated by Django 5.0.2 on 2024-03-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signupdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]