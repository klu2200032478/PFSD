# Generated by Django 5.0.2 on 2024-04-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_alter_postdetails_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('contactno', models.IntegerField()),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
    ]
