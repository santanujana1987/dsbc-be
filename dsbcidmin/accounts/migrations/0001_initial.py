# Generated by Django 4.0.5 on 2022-07-04 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_type', models.CharField(choices=[('purchase', 'Purchase'), ('sale', 'Sale'), ('credit_note', 'Credit Note'), ('debit_note', 'Debit Note'), ('contra', 'Contra'), ('receipt', 'Receipt'), ('payment', 'Payment'), ('journal', 'Journal')], default='journal', max_length=20)),
                ('journal_no', models.CharField(max_length=100)),
                ('transaction_no', models.CharField(max_length=100)),
                ('naration', models.CharField(max_length=500)),
                ('post_datetime', models.DateTimeField()),
                ('total_amount', models.FloatField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='journals_client_id', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='journals_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='journals_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='journals_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='journals_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_title', models.CharField(max_length=200)),
                ('type_code', models.CharField(max_length=20)),
                ('type_initial', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(max_length=200)),
                ('ledger_phone_no', models.CharField(max_length=20)),
                ('ledger_address', models.TextField()),
                ('opening_balance', models.FloatField()),
                ('ledger_balance', models.FloatField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_client_id', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_deleted_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LedgerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10)),
                ('no_of_group', models.IntegerField(default=0)),
                ('dr', models.CharField(max_length=10)),
                ('cr', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LedgerTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_type_title', models.CharField(max_length=200)),
                ('ledger_type_code', models.CharField(max_length=6)),
                ('final_account_section', models.CharField(blank=True, choices=[('tb', 'Trial Balance'), ('pl', 'Profite & Loss'), ('bs', 'Balance Sheet'), ('mf', 'Manufacturing')], default=None, max_length=3, null=True)),
                ('side', models.CharField(blank=True, choices=[('cr', 'Credit'), ('dr', 'Debit'), ('as', 'Asset'), ('lb', 'Liability')], default=None, max_length=6, null=True)),
                ('ordering', models.IntegerField(default=0)),
                ('ledger_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgercategory')),
            ],
        ),
        migrations.CreateModel(
            name='LedgerTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(verbose_name='date published')),
                ('crdr_type', models.CharField(choices=[('cr', 'Credit'), ('dr', 'Debit')], default='cr', max_length=10)),
                ('ledger_before_balance', models.FloatField()),
                ('amount', models.FloatField()),
                ('ledger_after_balance', models.FloatField()),
                ('transaction_no', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_client_id', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.journals')),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_from_ledger', to='accounts.ledger')),
                ('target_ledger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_to_ledger', to='accounts.ledger')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_transaction_history_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LedgerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_group_name', models.CharField(max_length=200)),
                ('ledger_group_code', models.CharField(max_length=10)),
                ('no_of_subgroup', models.IntegerField(default=0)),
                ('no_of_ledger', models.IntegerField(default=0)),
                ('nesting_level', models.IntegerField(blank=True, default=None, null=True)),
                ('editable', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledger_group_created_by', to=settings.AUTH_USER_MODEL)),
                ('ledger_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgercategory')),
                ('ledger_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgertypes')),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgergroup')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_group_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ledger',
            name='ledger_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgercategory'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='ledger_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgergroup'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='ledger_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledgertypes'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ledger_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='JournalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.FloatField()),
                ('drcr', models.CharField(choices=[('cr', 'Credit'), ('dr', 'Debit')], default='cr', max_length=2)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.journals')),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ledger')),
            ],
        ),
    ]
