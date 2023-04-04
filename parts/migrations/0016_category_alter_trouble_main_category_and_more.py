# Generated by Django 4.0.4 on 2023-03-19 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0015_alter_bigcategory_name_alter_smallcategory_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='trouble',
            name='main_category',
            field=models.CharField(choices=[('フリーザー', 'フリーザー'), ('ロボット', 'ロボット'), ('コンベア', 'コンベア'), ('その他', 'その他')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trouble',
            name='sub_category',
            field=models.CharField(choices=[('インレット', 'インレット'), ('アウトレット', 'アウトレット'), ('ベルト', 'ベルト'), ('ロボット', 'ロボット'), ('コンベア', 'コンベア'), ('その他', 'その他')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='BigCategory',
        ),
        migrations.DeleteModel(
            name='SmallCategory',
        ),
        migrations.AddField(
            model_name='trouble',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parts.category'),
        ),
    ]
