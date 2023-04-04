# Generated by Django 4.0.4 on 2023-03-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0004_tag_order_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='parts',
            name='tag',
            field=models.ManyToManyField(to='parts.tag'),
        ),
    ]
