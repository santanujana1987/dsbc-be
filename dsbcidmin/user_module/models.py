from django.db import models
from django.contrib.auth.models import User
from organization_module.models import DepartmentMaster
from dsbcidmin.custom import ChoiseClass # new
# Create your models here.
    

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_profile_user_id')
    tl_id = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_profile_tl_id',default=None,null=True)
    rm_id = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_profile_rm_id',default=None,null=True)
    mother_department = models.ForeignKey(DepartmentMaster,on_delete=models.PROTECT,related_name='user_mother_department_id',null=True,default=None)
    emp_code = models.IntegerField(unique=True)
    wallet_balance = models.FloatField(default=0.00)
    contact_no = models.CharField(max_length=20)
    address = models.TextField(null=True,blank=True)
    profile_image_id=models.CharField(max_length=200,null=True,blank=True)
    uplines = models.TextField(null=True,blank=True)
    
class UserGoals(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_goals_user_id')
    goal_initiator = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_goals_initiator_user_id',default=0)
    targeted_date = models.DateTimeField()
    target_amount = models.FloatField(default=0.00)
    achived_amount = models.FloatField(default=0.00)
    completion_date = models.DateTimeField()
    notes = models.TextField()
    created_at = models.DateField(auto_now=True)
    status = models.CharField(choices=ChoiseClass.STATUS_CHOISE,default='active',max_length=20)

class UserDepartment(models.Model):
    department = models.ForeignKey(DepartmentMaster,on_delete=models.PROTECT,related_name='user_department_department_id')
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_department_user_id')
    status = models.CharField(choices=ChoiseClass.STATUS_CHOISE,default='active',max_length=20)
    created_at = models.DateField(auto_now=True)
    credted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_department_created_by')
    updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_department_updated_by',default=None,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_department_deleted_by',default=None,blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True)