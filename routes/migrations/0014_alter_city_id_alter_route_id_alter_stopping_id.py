# Generated by Django 4.1.2 on 2022-12-05 23:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0013_alter_city_id_alter_route_id_alter_stopping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.UUID('421b8af3-487a-4179-9ce9-3a2bbd453e15'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.UUIDField(default=uuid.UUID('de81ce9e-088e-4375-9fa1-e8dec9194492'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stopping',
            name='id',
            field=models.UUIDField(default=uuid.UUID('af061f4c-5dc4-441c-9c22-9cd836f49a33'), editable=False, primary_key=True, serialize=False),
        ),
    ]
