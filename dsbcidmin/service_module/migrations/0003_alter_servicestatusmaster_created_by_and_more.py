# Generated by Django 4.0.5 on 2022-07-04 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service_module', '0002_servicestatusmaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicestatusmaster',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ssm_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicestatusmaster',
            name='deleted_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ssm_deleted_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicestatusmaster',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ssm_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
