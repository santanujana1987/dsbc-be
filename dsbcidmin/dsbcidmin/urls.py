from collections import UserList
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from accounts.master.ledger_group_view import LedgerGroupViewSet
from accounts.master.ledger_type_views import LedgerTypesViewSet
from accounts.models import *
from rest_framework.authtoken import views
from rest_framework.permissions import IsAuthenticated # new import

from accounts.views import UserViewSet
from accounts.master.ledger_category_views import LedgerCategoryViewSet

router = routers.DefaultRouter()

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', UserViewSet)


# LedgerCategory Routers provide an easy way of automatically determining the URL conf.
router.register(r'ledger-category', LedgerCategoryViewSet)
router.register(r'ledger-types', LedgerTypesViewSet)
router.register(r'ledger-groups', LedgerGroupViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/token-auth/',views.obtain_auth_token),
    path("accounting/", include('accounts.urls'))
]