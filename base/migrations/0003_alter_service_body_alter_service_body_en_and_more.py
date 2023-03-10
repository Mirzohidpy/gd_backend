# Generated by Django 4.1.4 on 2022-12-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_partner_title_en_partner_title_ru_partner_title_uz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='body',
            field=models.TextField(max_length=250, verbose_name='Kontent'),
        ),
        migrations.AlterField(
            model_name='service',
            name='body_en',
            field=models.TextField(max_length=250, null=True, verbose_name='Kontent'),
        ),
        migrations.AlterField(
            model_name='service',
            name='body_ru',
            field=models.TextField(max_length=250, null=True, verbose_name='Kontent'),
        ),
        migrations.AlterField(
            model_name='service',
            name='body_uz',
            field=models.TextField(max_length=250, null=True, verbose_name='Kontent'),
        ),
    ]
