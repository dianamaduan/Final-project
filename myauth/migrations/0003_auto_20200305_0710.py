# Generated by Django 3.0.3 on 2020-03-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumber', models.CharField(max_length=12, unique=True)),
                ('cvv', models.IntegerField()),
                ('balance', models.FloatField()),
                ('validDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='cards',
            field=models.ManyToManyField(to='myauth.Cards'),
        ),
    ]
