# Generated by Django 2.2.10 on 2020-06-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]