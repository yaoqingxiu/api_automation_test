# Generated by Django 2.0.2 on 2018-03-06 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0004_auto_20180314_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiparameterraw',
            name='api',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestParameterRaw', to='api_test.ApiInfo', verbose_name='所属接口'),
        ),
    ]
