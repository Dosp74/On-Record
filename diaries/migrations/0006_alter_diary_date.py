# Generated by Django 5.1.5 on 2025-02-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0005_diary_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
