# Generated by Django 2.1.7 on 2019-02-18 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190218_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumer_db',
            old_name='Role_Id',
            new_name='RId',
        ),
    ]
