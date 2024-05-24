# Generated by Django 4.2.13 on 2024-05-24 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_mother_material_alter_raw_material_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw_material',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother_material', to='users.mother_material'),
        ),
    ]
