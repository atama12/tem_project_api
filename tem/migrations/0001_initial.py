# Generated by Django 3.2.7 on 2021-10-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField()),
                ('version', models.IntegerField()),
                ('report_name', models.TextField()),
            ],
        ),
    ]
