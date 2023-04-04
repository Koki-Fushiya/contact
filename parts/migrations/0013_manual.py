# Generated by Django 4.0.4 on 2023-03-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0012_alter_parts_options_alter_trouble_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='download/')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
