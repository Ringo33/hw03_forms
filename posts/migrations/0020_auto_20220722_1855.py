# Generated by Django 2.2.9 on 2022-07-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Добавьте комментарий к посту', max_length=1000, verbose_name='Комментарий к посту'),
        ),
    ]