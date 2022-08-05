from queue import Empty
from rest_framework import serializers
from accounts.models import LedgerTypes

# Serializers define the API representation.
class LedgerTypesSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self, instance=None, data=Empty, **kwargs):
        if instance:
            setattr(self.Meta, 'depth', 1)
        else:
            setattr(self.Meta, 'depth', 0)
        super(LedgerTypesSerializer, self).__init__(instance, data, **kwargs)

    class Meta:
        model = LedgerTypes
        depth = 0
        fields = ['id','url','ledger_type_title', 'ledger_type_code', 'final_account_section', 'side','ordering','ledger_category']
        #fields = '__all__'

    def __str__(self):
        return '%d: %s' % (self.id, self.ledger_type_title)
