# Generated by Django 5.1.5 on 2025-02-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0008_diary_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
