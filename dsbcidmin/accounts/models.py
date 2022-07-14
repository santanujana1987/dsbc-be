from django.db import models
from django.contrib.auth.models import User # new
# from client.model import models
# Create your models here.

class LedgerCategory(models.Model):
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=10)
	no_of_group = models.IntegerField(default=0)
	dr = models.CharField(max_length=10)
	cr = models.CharField(max_length=10)

class LedgerTypes(models.Model):
	ledger_type_title = models.CharField(max_length=200)
	ledger_type_code = models.CharField(max_length=6)
	final_account_section = models.CharField(max_length=3,default=None,blank=True, null=True,choices=(('tb','Trial Balance'),('pl','Profite & Loss'),('bs','Balance Sheet'),('mf','Manufacturing')))
	side = models.CharField(max_length=6,default=None,blank=True, null=True,choices=(('cr','Credit'),('dr','Debit'),('as','Asset'),('lb','Liability')))
	ordering = models.IntegerField(default=0)
	ledger_category = models.ForeignKey("LedgerCategory",on_delete=models.PROTECT,related_name="ledger_type")

class LedgerGroup(models.Model):
	ledger_group_name = models.CharField(max_length=200)
	ledger_category = models.ForeignKey("LedgerCategory",on_delete=models.PROTECT)
	ledger_type = models.ForeignKey("LedgerTypes",on_delete=models.PROTECT)
	parent_group = models.ForeignKey("LedgerGroup",on_delete=models.PROTECT)
	ledger_group_code = models.CharField(max_length=10)
	no_of_subgroup = models.IntegerField(default=0)
	no_of_ledger = models.IntegerField(default=0)
	nesting_level = models.IntegerField(default=None,blank=True, null=True)
	editable = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_group_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_group_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	
class Ledger(models.Model):
	ledger_category = models.ForeignKey("LedgerCategory",on_delete=models.PROTECT)
	ledger_type = models.ForeignKey("LedgerTypes",on_delete=models.PROTECT)
	ledger_group = models.ForeignKey("LedgerGroup",on_delete=models.PROTECT)
	client = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_client_id',default=0)
	ledger_name = models.CharField(max_length=200)
	ledger_phone_no = models.CharField(max_length=20)
	ledger_address = models.TextField()
	opening_balance = models.FloatField()
	ledger_balance = models.FloatField()
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class JournalTypes(models.Model):
	type_title = models.CharField(max_length=200)
	type_code = models.CharField(max_length=20)
	type_initial = models.CharField(max_length=20)

class Journals(models.Model):
	journal_type = models.CharField(max_length=20,choices=(('purchase','Purchase'),('sale','Sale'),('credit_note','Credit Note'),('debit_note','Debit Note'),('contra','Contra'),('receipt','Receipt'),('payment','Payment'),('journal','Journal')),default='journal')
	journal_no = models.CharField(max_length=100)
	transaction_no = models.CharField(max_length=100)
	naration = models.CharField(max_length=500)
	client = models.ForeignKey(User,on_delete=models.PROTECT,related_name='journals_client_id',default=0)
	user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='journals_user_id')
	post_datetime = models.DateTimeField(auto_now=False)
	total_amount = models.FloatField();
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='journals_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='journals_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='journals_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)

class JournalDetails(models.Model):
	journal = models.ForeignKey("Journals", on_delete=models.PROTECT)
	ledger= models.ForeignKey("Ledger", on_delete=models.PROTECT)
	transaction_amount = models.FloatField()
	drcr = models.CharField(max_length=2,choices=(('cr','Credit'),('dr','Debit')),default='cr')


class LedgerTransactionHistory(models.Model):
	transaction_date = models.DateTimeField('date published')
	journal = models.ForeignKey("Journals",on_delete=models.PROTECT)
	client = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_transaction_history_client_id',default=0)
	user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_transaction_history_user_id')
	ledger = models.ForeignKey(Ledger,on_delete=models.PROTECT,related_name='ledger_transaction_history_from_ledger')
	target_ledger = models.ForeignKey(Ledger,on_delete=models.PROTECT,related_name='ledger_transaction_history_to_ledger')
	crdr_type = models.CharField(choices=(('cr','Credit'),('dr','Debit')),default='cr',max_length=10)
	ledger_before_balance = models.FloatField()
	amount = models.FloatField()
	ledger_after_balance = models.FloatField()
	transaction_no = models.CharField(max_length=100)
	note = models.CharField(max_length=500)
	status = models.CharField(choices=(('active','active'),('inactive','inactive'),('deleted','deleted')),default='active',max_length=10)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_transaction_history_created_by')
	created_at = models.DateTimeField('date published')
	updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_transaction_history_updated_by',default=None,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='ledger_transaction_history_deleted_by',default=None,blank=True, null=True)
	deleted_at = models.DateTimeField(auto_now=True)
