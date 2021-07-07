# Generated by Django 3.2.3 on 2021-07-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': ('категория',),
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='фото товара')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='карткое описание товара')),
                ('description', models.TextField(blank=True, verbose_name='описание продукта')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': ('продукт',),
                'verbose_name_plural': 'продукты',
            },
        ),
    ]