# Generated by Django 2.2.5 on 2020-05-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20200511_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='tel_no',
            field=models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]