# Generated by Django 4.0.3 on 2022-03-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('category_logo', models.ImageField(default='default.png', upload_to='images')),
                ('sub_category1', models.CharField(max_length=255)),
                ('sub_category2', models.CharField(max_length=255)),
                ('sub_category3', models.EmailField(max_length=255)),
                ('sub_category4', models.CharField(max_length=255)),
                ('sub_category5', models.CharField(max_length=255)),
            ],
        ),
    ]