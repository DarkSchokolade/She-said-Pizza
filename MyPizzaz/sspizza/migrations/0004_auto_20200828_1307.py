# Generated by Django 3.1 on 2020-08-28 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sspizza', '0003_auto_20200828_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('VEG', 'VEG'), ('NON-VEG', 'NON-VEG')], max_length=10)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customerinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='baseCrust',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='nonVegToppings',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='order',
            name='vegToppings',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Base',
        ),
        migrations.DeleteModel(
            name='CustomerInfo',
        ),
        migrations.DeleteModel(
            name='NonVegTopping',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='VegTopping',
        ),
        migrations.AddField(
            model_name='pizza',
            name='crust',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sspizza.crust'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='topping',
            field=models.ManyToManyField(to='sspizza.Topping'),
        ),
    ]
