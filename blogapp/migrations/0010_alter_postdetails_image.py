# Generated by Django 5.0.2 on 2024-03-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_postdetails_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdetails',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
