# Generated by Django 3.0.3 on 2020-03-11 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0008_auto_20200311_0420'),
        ('items', '0003_auto_20200311_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myauth.Users'),
        ),
    ]
