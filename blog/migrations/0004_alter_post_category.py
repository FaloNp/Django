# Generated by Django 5.0.1 on 2024-01-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('ITEM1', 'Tech & IT'), ('ITEM2', 'Hobbies & Fun'), ('ITEM3', 'Sports & Rec'), ('ITEM4', 'Cooking & Food'), ('ITEM5', 'Art & Culture')], default='ITEM1', max_length=50),
        ),
    ]
