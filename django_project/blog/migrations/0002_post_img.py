# Generated by Django 2.1.7 on 2019-03-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
    ]
