# Generated by Django 3.0.5 on 2020-05-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpsite', '0002_auto_20200507_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_title', models.CharField(max_length=100)),
                ('cycle_description', models.TextField()),
                ('cycle_year', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='verse',
            name='verse_cycle',
            field=models.ManyToManyField(to='vpsite.Cycle'),
        ),
    ]
