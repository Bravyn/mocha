# Generated by Django 5.0.4 on 2024-04-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polkadot', '0004_rename_name_imagemodel_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='comments',
            field=models.TextField(help_text='Type some few comments about the picture', max_length=255),
        ),
    ]
