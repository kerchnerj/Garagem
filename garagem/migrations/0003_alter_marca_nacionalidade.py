# Generated by Django 4.1.7 on 2023-03-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
