from dataclasses import field
from rest_framework import serializers
from accounts.models import LedgerGroup

# Serializers define the API representation.

class LedgerGroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LedgerGroup
        fields = ['id','ledger_group_name','ledger_category', 'ledger_type', 'parent_group', 'ledger_group_code','no_of_subgroup','no_of_ledger','nesting_level']

    def __str__(self):
        return '%d: %s' % (self.id, self.ledger_type_title)
