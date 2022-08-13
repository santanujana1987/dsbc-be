from django.urls import path

from accounts.master.ledger_category_custom_views import AccountingCustomEndPoints

urlpatterns = [
    path('ledger-type-category',AccountingCustomEndPoints.as_view(),name='ledger-type-category')
]
