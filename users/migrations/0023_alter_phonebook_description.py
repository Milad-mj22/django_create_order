# Generated by Django 4.1.2 on 2023-07-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0022_merge_20230707_2112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonebook",
            name="description",
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
