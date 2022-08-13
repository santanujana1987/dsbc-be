from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.

class ServiceGroup(models.Model):
	service_group_title = models.CharField(max_length=200)
	no_of_service = models.IntegerField(default=0)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='sg_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='sg_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='sg_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class ServiceType(models.Model):
	service_type_name = models.CharField(max_length=255)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='st_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='st_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='st_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class RenewalPattern(models.Model):
	renewal_pattern_name = models.CharField(max_length=200)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='rp_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='rp_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='rp_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class RenewalPatternDetails(models.Model):
	renewal_pattern_id = models.ForeignKey("RenewalPattern",on_delete=models.CASCADE)
	frequency_name = models.CharField(max_length=200)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='rpd_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='rpd_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='rpd_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class ServiceMaster(models.Model):
	service_group = models.ForeignKey("ServiceGroup",on_delete=models.PROTECT)
	renewal_pattern = models.ForeignKey("RenewalPattern",on_delete=models.PROTECT)
	service_type = models.ForeignKey("ServiceType",on_delete=models.PROTECT)
	service_name = models.CharField(max_length=200)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='sm_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='sm_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='sm_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class ServiceStatusMaster(models.Model):
	service = models.ForeignKey(ServiceMaster,on_delete=models.PROTECT)
	status_title = models.CharField(max_length=200)
	status_order = models.IntegerField(default=0)
	status_percentage = models.IntegerField(default=0)
	color = models.CharField(max_length=50,default='#5cb85c')
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ssm_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ssm_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ssm_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)