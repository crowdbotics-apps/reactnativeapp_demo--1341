# Generated by Django 2.2.9 on 2019-12-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_customtext_test"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customtext",
            name="test",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
