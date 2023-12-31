# Generated by Django 4.2.6 on 2023-10-20 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_created_at_book_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_lang', models.TextField()),
                ('text_review', models.TextField()),
                ('rate_stars', models.CharField(choices=[('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_object', to='book.book')),
            ],
        ),
    ]
