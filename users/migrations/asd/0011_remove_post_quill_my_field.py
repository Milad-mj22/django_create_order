# Generated by Django 4.1.2 on 2023-06-14 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_post_quill_my_field_alter_quillpost_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_quill',
            name='my_field',
        ),
    ]