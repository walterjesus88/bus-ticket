# Generated by Django 4.1.2 on 2022-12-02 00:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0007_alter_city_id_alter_route_id_alter_stopping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.UUID('98e6a8fd-05cc-4f6b-868a-4d17b576ba9d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ca69538c-98b9-4ba9-9b7c-1787de40c6ab'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stopping',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8117dffa-78e5-46cf-831f-f636ddd3656b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
