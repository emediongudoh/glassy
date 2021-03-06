# Generated by Django 4.0.5 on 2022-07-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
