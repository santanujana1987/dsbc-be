from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from accounts.models import *
from rest_framework.authtoken import views
from rest_framework.permissions import IsAuthenticated # new import

from accounts.views import UserViewSet

router = routers.DefaultRouter()

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', UserViewSet)

## LedgerCategory Start 

# Serializers define the API representation.
class LedgerCategorySerializer(serializers.HyperlinkedModelSerializer):
    #ledger_types = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #ledger_types = serializers.PrimaryKeyRelatedField(queryset=LedgerTypes.objects.all(),many=True) 
    class Meta:
        model = LedgerCategory
        fields = ['url','name', 'code', 'cr', 'dr','no_of_group']

# LedgerCategory ViewSets define the view behavior.
class LedgerCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
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


## LedgerGroup Start 

# Serializers define the API representation.
class LedgerGroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LedgerGroup
        fields = ['id','ledger_group_name','ledger_category', 'ledger_type', 'parent_group', 'ledger_group_code','no_of_subgroup','no_of_ledger','nesting_level']

    def __str__(self):
        return '%d: %s' % (self.id, self.ledger_type_title)
# ViewSets define the view behavior.
class LedgerGroupViewSet(viewsets.ModelViewSet):
    queryset = LedgerGroup.objects.all()
    serializer_class = LedgerGroupSerializer

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'ledger-groups', LedgerGroupViewSet)

## LedgerGroup End



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/token-auth/',views.obtain_auth_token)
]