# Generated by Django 3.2.7 on 2022-02-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0011_alter_member_baptised'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'member', 'verbose_name_plural': 'members'},
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]