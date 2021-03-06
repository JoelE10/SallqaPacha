# Generated by Django 3.0 on 2021-12-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objetivosonu', '0008_auto_20211218_0200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_added',
            new_name='created',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=False, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80),
        ),
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
        migrations.DeleteModel(
            name='Like',
        ),
    ]
