# Generated by Django 3.2.7 on 2022-01-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.TextField()),
                ('date_reg', models.DateTimeField(auto_now_add=True)),
                ('did_by', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('type_of', models.CharField(choices=[('GIVING', 'Giving'), ('DONATION', 'Donation'), ('WITHDRAWAL', 'Withdrawal')], max_length=250)),
            ],
        ),
    ]
