# Generated by Django 3.1.2 on 2020-10-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddstracker', '0004_add_created_and_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odds',
            name='mkt_type',
            field=models.CharField(choices=[('H2H', 'h2h'), ('H2H_LAY', 'h2h_lay'), ('SPREAD', 'spread'), ('TOTALS', 'totals')], max_length=100),
        ),
    ]
