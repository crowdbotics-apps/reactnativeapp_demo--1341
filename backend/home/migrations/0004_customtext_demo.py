# Generated by Django 2.2.9 on 2019-12-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191230_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='demo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
