# Generated by Django 3.1 on 2020-09-10 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sspizza', '0010_auto_20200907_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('food_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ordercart',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sspizza.menu'),
        ),
    ]
