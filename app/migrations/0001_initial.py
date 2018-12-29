# Generated by Django 2.1.3 on 2018-12-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]