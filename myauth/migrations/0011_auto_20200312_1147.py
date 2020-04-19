# Generated by Django 3.0.3 on 2020-03-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0010_remove_users_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='cardBalance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='cardBalance',
            field=models.FloatField(default=0),
        ),
    ]
