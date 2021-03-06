# Generated by Django 4.0.2 on 2022-04-07 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelSales',
            fields=[
                ('id', models.BigAutoField(db_column='id', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='date_creation')),
                ('name', models.CharField(db_index=True, max_length=35, verbose_name='name_of_client')),
                ('description', models.CharField(db_index=True, max_length=300, verbose_name='description_product')),
                ('count', models.PositiveIntegerField(db_index=True, verbose_name='count')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10, verbose_name='price')),
                ('paid_out', models.BooleanField(db_index=True, default=True, verbose_name='paid_out')),
                ('total', models.FloatField(db_index=True, default=0.0, verbose_name='total')),
            ],
            options={
                'db_table': 'tienda_lissa_table',
            },
        ),
    ]
