# Generated by Django 4.1.5 on 2023-05-20 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('testaus', '0004_malli1_malli2'),
    ]

    operations = [
        migrations.AddField(
            model_name='malli1',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AddField(
            model_name='malli2',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='malli1',
            name='answer',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='malli1',
            name='empty',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='malli1',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='malli2',
            name='answer',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='malli2',
            name='empty',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='malli2',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
