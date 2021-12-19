# Generated by Django 3.0 on 2021-12-18 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objetivosonu', '0011_auto_20211218_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='objetivosonu.Post'),
        ),
        migrations.AlterField(
            model_name='postview',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objetivosonu.Post'),
        ),
    ]