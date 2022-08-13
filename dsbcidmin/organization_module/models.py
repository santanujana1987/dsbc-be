from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.
class OrganizationMaster(models.Model):
	organization_name = models.CharField(max_length=200)
	organization_address = models.TextField()
	contact_no = models.CharField(max_length=20)
	email_id = models.CharField(max_length=200)
	web_address = models.CharField(max_length=200)

class DepartmentMaster(models.Model):
	organization = models.ForeignKey(OrganizationMaster,on_delete=models.PROTECT,related_name='department_organization')
	department_name = models.CharField(max_length=200)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='department_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='department_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(default=None,blank=True, null=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='department_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(default=None,blank=True, null=True)

class DesignationMaster(models.Model):
	organization = models.ForeignKey(OrganizationMaster,on_delete=models.PROTECT,related_name='designation_organization')
	designation_name = models.CharField(max_length=200)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='designation_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='designation_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='designation_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(default=None,blank=True, null=True)

class DepartmentDesignationRelation(models.Model):
	organization = models.ForeignKey(OrganizationMaster,on_delete=models.PROTECT,related_name='ddr_organization')
	departmant = models.ForeignKey(DepartmentMaster,on_delete=models.PROTECT,related_name='ddr_department')
	designation = models.ForeignKey(DesignationMaster,on_delete=models.PROTECT,related_name='ddr_designation')
	level = models.IntegerField(default=0)
	status = models.CharField(choices=(('assigned','assigned'),('unassigned','unassigned')),default='assigned',max_length=10)
	assigned_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ddr_assigned_by')
	assigned_at = models.DateTimeField('date published')
	unassigned_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ddr_unassigned_by',default=None,blank=True, null=True)
	unassigned_at = models.DateTimeField(default=None,blank=True, null=True)

class DepartmentDesignationRelationChangeLog(models.Model):
	organization = models.ForeignKey(OrganizationMaster,on_delete=models.PROTECT,related_name='ddrcg_organization')
	departmant = models.ForeignKey(DepartmentMaster,on_delete=models.PROTECT,related_name='ddrcg_department')
	designation = models.ForeignKey(DesignationMaster,on_delete=models.PROTECT,related_name='ddrcg_designation')
	from_level = models.IntegerField(default=0)
	to_level = models.IntegerField(default=0)
	chnage_type = models.CharField(choices=(('added','added'),('modified','modified'),('deleted','deleted')),default='added',max_length=10)
	changed_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ddrcg_changed_by')
	changed_at = models.DateTimeField('date published')