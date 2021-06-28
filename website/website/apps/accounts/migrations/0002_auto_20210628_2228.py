# Generated by Django 3.2.4 on 2021-06-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('normalized_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interest',
            field=models.ManyToManyField(blank=True, to='accounts.UserInterest'),
        ),
    ]
