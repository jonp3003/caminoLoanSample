# Generated by Django 2.0.7 on 2019-05-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('type', models.CharField(choices=[('', 'Select One'), ('fdt', 'Food Truck'), ('cst', 'Construction'), ('res', 'Restaurant'), ('bar', 'Barbershop'), ('oth', 'Other')], max_length=3)),
                ('years', models.IntegerField()),
            ],
        ),
    ]