# Generated by Django 4.0.4 on 2022-05-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_category_galleria_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleria',
            name='image_pic',
        ),
        migrations.AddField(
            model_name='galleria',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
