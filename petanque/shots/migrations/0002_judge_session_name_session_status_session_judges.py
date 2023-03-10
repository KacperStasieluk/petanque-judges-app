# Generated by Django 4.1.5 on 2023-01-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('license_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='name',
            field=models.CharField(default='defaultname', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(default='active', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='judges',
            field=models.ManyToManyField(to='shots.judge'),
        ),
    ]
