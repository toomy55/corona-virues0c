# Generated by Django 3.0.3 on 2020-04-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_avrage'),
    ]

    operations = [
        migrations.CreateModel(
            name='manths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
    ]
