# Generated by Django 4.1.5 on 2023-02-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='languageexample',
            name='tags',
            field=models.ManyToManyField(blank=True, to='languages.tag'),
        ),
    ]
