# Generated by Django 3.1.7 on 2021-03-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210301_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_Images',
            field=models.ImageField(upload_to='../media/blog-images/'),
        ),
    ]
