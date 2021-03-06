# Generated by Django 2.2.5 on 2020-05-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_auto_20200511_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('plan_name', models.CharField(max_length=100)),
                ('plan_amount', models.IntegerField()),
                ('plan_detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
