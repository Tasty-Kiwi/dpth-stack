# Generated by Django 4.2.6 on 2023-10-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlykiwis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='posted', to='onlykiwis.post'),
        ),
    ]
