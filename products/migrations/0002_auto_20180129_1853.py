# Generated by Django 2.0.1 on 2018-01-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]