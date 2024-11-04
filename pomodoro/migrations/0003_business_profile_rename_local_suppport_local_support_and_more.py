# Generated by Django 5.1.2 on 2024-11-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro', '0002_address_categories_contact_local_suppport_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='local_suppport',
            new_name='local_support',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
