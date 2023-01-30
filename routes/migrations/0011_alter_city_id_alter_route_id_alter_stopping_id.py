# Generated by Django 4.1.2 on 2022-12-02 00:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0010_alter_city_id_alter_route_id_alter_stopping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4f74380c-7bbe-4226-aa94-6ee2132c6c6d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.UUIDField(default=uuid.UUID('665f2bde-6e8b-4866-96c4-69a77752bce8'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stopping',
            name='id',
            field=models.UUIDField(default=uuid.UUID('464aeaad-8738-44c5-ab4c-ed709c52e6ad'), editable=False, primary_key=True, serialize=False),
        ),
    ]