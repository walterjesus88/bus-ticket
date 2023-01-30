# Generated by Django 4.1.2 on 2022-11-20 21:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_alter_city_id_alter_route_id_alter_stopping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.UUID('978aecbd-6bda-4bc6-aa12-05c434f2a151'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.UUIDField(default=uuid.UUID('219d8739-e888-4e37-877c-914a7f12a1bd'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stopping',
            name='id',
            field=models.UUIDField(default=uuid.UUID('905ce79a-331e-4721-ae4e-003eb57aa1d7'), editable=False, primary_key=True, serialize=False),
        ),
    ]