# Generated by Django 4.1.5 on 2023-05-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testaus', '0006_remove_malli1_empty_remove_malli2_empty_muistipeli_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='muistipeli',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
