from django.db import models
from django.contrib.auth.models import User

from dsbcidmin.custom import ChoiseClass

class DepartmentMaster(models.Model):
    department_name = models.CharField(max_length=200,unique=True)
    department_code = models.CharField(max_length=100,unique=True)
    status = models.CharField(choices=ChoiseClass.STATUS_CHOISE,default='active',max_length=10)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='department_master_created_by')
    created_at = models.DateTimeField('date published')
    updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='department_master_updated_by',default=None,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='department_master_deleted_by',default=None,blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True)

# Create your models here.
