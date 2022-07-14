from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from accounts.models import *

router = routers.DefaultRouter()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', UserViewSet)

## LedgerCategory Start 

# Serializers define the API representation.
class LedgerCategorySerializer(serializers.HyperlinkedModelSerializer):
    #ledger_types = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    ledger_types = serializers.PrimaryKeyRelatedField(queryset=LedgerTypes.objects.all(),many=True) 
    class Meta:
        model = LedgerCategory
        fields = ['url','name', 'code', 'cr', 'dr','ledger_types']

# LedgerCategory ViewSets define the view behavior.
class LedgerCategoryViewSet(viewsets.ModelViewSet):
    queryset = LedgerCategory.objects.all()
    serializer_class = LedgerCategorySerializer

# LedgerCategory Routers provide an easy way of automatically determining the URL conf.
router.register(r'ledger-category', LedgerCategoryViewSet)

## LedgerCategory End

## LedgerTypes Start 

# Serializers define the API representation.
class LedgerTypesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LedgerTypes
        fields = ['id','url','ledger_type_title', 'ledger_type_code', 'final_account_section', 'side','ordering','ledger_category']

    def __str__(self):
        return '%d: %s' % (self.id, self.ledger_type_title)
# ViewSets define the view behavior.
class LedgerTypesViewSet(viewsets.ModelViewSet):
    queryset = LedgerTypes.objects.all()
    serializer_class = LedgerTypesSerializer

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'ledger-types', LedgerTypesViewSet)

## LedgerTypes End

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]