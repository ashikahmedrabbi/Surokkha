# Generated by Django 5.0.1 on 2024-03-09 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccines', '0006_rename_book_review_vaccines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='second_dose_date',
        ),
    ]
