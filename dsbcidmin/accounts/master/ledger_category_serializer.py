# Serializers define the API representation.
from dataclasses import field
from rest_framework import serializers
from accounts.models import LedgerCategory, LedgerTypes


class LedgerCategorySerializer(serializers.HyperlinkedModelSerializer):
    lc_Ledger_types = serializers.StringRelatedField(many=True)
    class Meta:
        model = LedgerCategory
        fields = ['id','url','name', 'code', 'cr', 'dr','no_of_group','lc_Ledger_types']
        #fields = '__all__'
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)    

    def __unicode__(self):
        return self.name    
