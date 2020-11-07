# Generated by Django 3.1 on 2020-11-07 16:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('postcode', models.CharField(default='NE658UQ', max_length=60)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
