# Generated by Django 4.1.2 on 2022-11-20 21:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('304682ac-de83-4385-8444-da68ff0238e9'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('f724c24a-5663-4c50-8c1f-34e277882d57'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stopping',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('1ec42593-0570-4902-ab1b-4f3f2f80d27e'), editable=False, primary_key=True, serialize=False)),
                ('has_agency', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stoppings', to='routes.city')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.route')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='cities',
            field=models.ManyToManyField(through='routes.Stopping', to='routes.route'),
        ),
    ]
