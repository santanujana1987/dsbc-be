from django.contrib import admin

from accounts.models import LedgerCategory, LedgerGroup, LedgerTypes

# Register your models here.

@admin.register(LedgerCategory)
class LedgerCategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","code","cr","dr","no_of_group"]

@admin.register(LedgerTypes)
class LedgerTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LedgerTypes._meta.fields]

@admin.register(LedgerGroup)
class LedgerGroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LedgerGroup._meta.fields]