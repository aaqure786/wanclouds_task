# Generated by Django 3.2.6 on 2021-08-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostFound', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found_item',
            name='desciption',
            field=models.CharField(max_length=100, null=True),
        ),
    ]