# Generated by Django 4.1.5 on 2023-05-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testaus', '0009_alter_muistipeli_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muistipeli',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='users/'),
        ),
    ]
