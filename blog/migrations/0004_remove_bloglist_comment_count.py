# Generated by Django 5.0.1 on 2024-02-27 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglist',
            name='comment_count',
        ),
    ]
