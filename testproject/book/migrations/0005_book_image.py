# Generated by Django 4.2.7 on 2023-11-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='upload'),
        ),
    ]
