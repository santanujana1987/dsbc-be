# Generated by Django 4.0.5 on 2022-07-02 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RenewalPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renewal_pattern_name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_by', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_group_title', models.CharField(max_length=200)),
                ('no_of_service', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_by', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_by', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_by', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('renewal_pattern', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service_module.renewalpattern')),
                ('service_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service_module.servicegroup')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service_module.servicetype')),
            ],
        ),
        migrations.CreateModel(
            name='RenewalPatternDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency_name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')], default='active', max_length=10)),
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_by', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('renewal_pattern_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_module.renewalpattern')),
            ],
        ),
    ]