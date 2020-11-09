# Generated by Django 2.2 on 2020-11-08 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20201107_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_created_comments', to='src.User'),
        ),
    ]
