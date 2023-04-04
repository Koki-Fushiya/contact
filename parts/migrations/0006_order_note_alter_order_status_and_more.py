# Generated by Django 4.0.4 on 2023-03-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_remove_order_tag_parts_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('-1個/セット', '-1個/セット'), ('在庫切れ', '在庫切れ'), ('在庫数正常', '在庫数正常')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='parts',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]