# Generated by Django 2.2.5 on 2020-05-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20200511_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
