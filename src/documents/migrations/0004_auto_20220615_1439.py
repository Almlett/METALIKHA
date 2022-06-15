# Generated by Django 3.1.7 on 2022-06-15 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20220615_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='items',
        ),
        migrations.AddField(
            model_name='quoteitem',
            name='quote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='documents.quote'),
            preserve_default=False,
        ),
    ]
