# Generated by Django 4.2.6 on 2023-10-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='actuality',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='book',
            name='video',
        ),
        migrations.AddField(
            model_name='book',
            name='created_date_lang',
            field=models.DateField(null=True),
        ),
    ]
