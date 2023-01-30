# Generated by Django 4.1.2 on 2022-12-01 23:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_alter_city_id_alter_route_id_alter_stopping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7e02a1e-534e-46ec-a77d-5a1de0722de2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5267ef37-1d32-490b-a6c4-e5122e19211a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stopping',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1629e666-7c18-4275-9fe4-5cb281cc9a54'), editable=False, primary_key=True, serialize=False),
        ),
    ]