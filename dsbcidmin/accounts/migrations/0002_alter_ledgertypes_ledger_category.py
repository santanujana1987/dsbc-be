# Generated by Django 4.0.5 on 2022-07-12 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgertypes',
            name='ledger_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_type', to='accounts.ledgercategory'),
        ),
    ]
